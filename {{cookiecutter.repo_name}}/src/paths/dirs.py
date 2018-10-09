from os.path import abspath, join, pardir


# project
DIR_PROJECT = abspath(join(__file__, pardir, pardir, pardir))

# data
DIR_DATA = join(DIR_PROJECT, 'data')
DIR_DATA_EXTERNAL = join(DIR_DATA, 'external')
DIR_DATA_INTERIM = join(DIR_DATA, 'interim')
DIR_DATA_PROCESSED = join(DIR_DATA, 'processed')
DIR_DATA_RAW = join(DIR_DATA, 'raw')

# models
DIR_MODELS = join(DIR_PROJECT, 'models')

# notebooks
DIR_NOTEBOOKS = join(DIR_PROJECT, 'notebooks')

# reports & figures
DIR_REPORTS = join(DIR_PROJECT, 'reports')
DIR_REPORTS_FIGURES = join(DIR_REPORTS, 'figures')
