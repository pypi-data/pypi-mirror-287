# Django Graph Models Command

This package provides a Django custom management command to generate a graph of a model and its neighbors up to a specified depth.

## Installation

0. Make sure Graphviz is installed
> sudo apt-get update && sudo apt-get install graphviz graphviz-dev

1. Install the package using pip:
> pip install django-db-modeler

2. Add the app to your Django project's `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...,
    'db_modeler',
]
```


## Usage

> python manage.py model_db your_app.ModelName 1 --output output_file.svg

## Options

- model_name: The name of the model to visualize.
- depth: The depth of relationships to include.
- --output: The output file name.
- --theme: The theme to use for the graph (default: original).
- --layout: The layout of the graph (default: dot).

## Example 

> python manage.py model_db product.Product 1 --output model.svg

## License 

This project is licensed under the MIT License. 