from pathlib import Path

# project
DIR_PROJECT = Path(__file__)
while DIR_PROJECT.name != '{{cookiecutter.repo_name}}':
    DIR_PROJECT = DIR_PROJECT.parent

# data
DIR_DATA = DIR_PROJECT / 'data'
DIR_DATA_EXTERNAL = DIR_DATA / 'external'
DIR_DATA_INTERIM = DIR_DATA / 'interim'
DIR_DATA_PROCESSED = DIR_DATA / 'processed'
DIR_DATA_RAW = DIR_DATA / 'raw'

# models
DIR_MODELS = DIR_PROJECT / 'models'

# notebooks
DIR_NOTEBOOKS = DIR_PROJECT / 'notebooks'

# figures
DIR_FIGURES = DIR_PROJECT / 'figures'
