from os.path import abspath, join, pardir


# project
dir_project = abspath(join(__file__, pardir, pardir, pardir))

# data
dir_data = join(dir_project, 'data')
dir_data_external = join(dir_data, 'external')
dir_data_interim = join(dir_data, 'interim')
dir_data_processed = join(dir_data, 'processed')
dir_data_raw = join(dir_data, 'raw')

# models
dir_models = join(dir_project, 'models')

# notebooks
dir_notebooks = join(dir_project, 'notebooks')

# reports & figures
dir_reports = join(dir_project, 'reports')
dir_reports_figures = join(dir_reports, 'figures')

