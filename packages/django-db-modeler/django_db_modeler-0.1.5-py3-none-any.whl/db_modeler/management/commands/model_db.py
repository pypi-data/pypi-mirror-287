import warnings
import django
django.setup()
from django.core.management.base import BaseCommand
from django.apps import apps
from django_extensions.management.commands.graph_models import (
    Command as GraphModelsCommand,
)

class Command(BaseCommand):
    help = "Generate a graph of a model and its neighbors up to a specified depth"

    def add_arguments(self, parser):
        parser.add_argument(
            "model_name", type=str, help="The name of the model to visualize"
        )
        parser.add_argument(
            "depth", type=int, help="The depth of relationships to include"
        )
        parser.add_argument("--output", type=str, default=None, help="The output file")
        parser.add_argument(
            "--theme",
            type=str,
            default="original",
            help="The theme to use for the graph. One of: original, table, or notebook",
        )
        parser.add_argument(
            "--layout",
            type=str,
            default="dot",
            help="How the graphs should be arranged. One of: dot, neato, twopi, circo, fdp, or nop",
        )

    def handle(self, *args, **options):
        warnings.filterwarnings("ignore")
        model_name = options["model_name"]
        depth = options["depth"]
        output = options["output"]
        if output is None:
            output = f"{model_name}_{depth}.svg"
        theme = options["theme"]
        layout = options["layout"]
        model_name_only = model_name.split(".")[1]

        print("--- Building graph connections from root model: ", model_name)
        print("--- Depth of included neighbors: ", depth)

        app_models = apps.get_models()
        model_dict = {model._meta.label: model for model in app_models}
        if model_name not in model_dict:
            self.stdout.write(self.style.ERROR(f'Model "{model_name}" not found.'))
            return

        def get_related_models(model, current_depth):
            if current_depth >= depth:
                return set()
            related_models = set()
            for field in model._meta.get_fields():
                if field.is_relation and field.related_model:
                    related_models.add(field.related_model)
                    related_models.update(
                        get_related_models(field.related_model, current_depth + 1)
                    )
            return related_models

        target_model = model_dict[model_name]
        selected_models = {target_model}
        selected_models.update(get_related_models(target_model, 0))

        selected_model_names = [
            model._meta.label.split(".")[1] for model in selected_models
        ]
        if depth == 1:
            print(f"--- Direct neighbors of {model_name_only}:")
            neighbors = selected_model_names.copy()
            neighbors.remove(model_name_only)
            for model in neighbors:
                print(f"    - {model}")
        else:
            print(f"--- Models to be visualized:")
            for model in selected_model_names:
                print(f"    - {model}")
        print("--- Number of models included in graph: ", len(selected_models))

        graph_models_cmd = GraphModelsCommand()
        graph_models_cmd.handle(
            app_label=[],
            outputfile=output,
            include_models=selected_model_names,
            theme=theme,
            layout=layout,
            group_models=False,
            all_applications=True,
            inheritance=False,
            no_inherited=False,
            no_color=False,
            verbose=False,
            relation_fields_only=True,
        )

        self.stdout.write(
            self.style.SUCCESS(f"--- Graph generated and saved to {output}")
        )
