pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'sleepcover')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)
conf.set('APP_ID', application_id)

configure_file(
  input: 'sleepcover.in',
  output: 'sleepcover',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

sleepcover_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(sleepcover_sources, install_dir: moduledir)
