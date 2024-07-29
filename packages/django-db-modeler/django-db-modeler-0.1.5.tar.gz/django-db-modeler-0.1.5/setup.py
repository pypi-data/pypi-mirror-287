from setuptools import setup, find_packages

setup(
    name='django-db-modeler',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'django-extensions>=3.0',
        'pygraphviz==1.13',
    ],
    entry_points={
        'console_scripts': [
            'model_db=db_modeler.management.commands.model_db:Command',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    description='A Django management command to generate a graph of a model and its neighbors up to a specified depth.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django-graph-models-command',
    author='Felix Lohrke',
    author_email='Sontyp@bin-wieder-da.de',
    license='MIT',
)
