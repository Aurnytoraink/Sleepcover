project(
  'sleepcover',
  version: '0.1',
  meson_version: '>= 0.59.0',
  license: ['GPL-3.0-or-later'],
)


# Dependencies
dependency('gtk4', version: '>= 4.5.0')
dependency('libadwaita-1', version: '>=1.0')

gnome = import('gnome')
i18n = import('i18n')
python = import('python').find_installation('python3')

prefix = get_option('prefix')

# Development mode
if get_option('devel') == true
  profile = '.Devel'
else
  profile = ''
endif

BASE_ID = 'com.github.Aurnytoraink.Sleepcover'
APP_ID = 'com.github.Aurnytoraink.Sleepcover@0@'.format(profile)

bindir = prefix / get_option('bindir')
datadir = prefix / get_option('datadir')
localedir = prefix / get_option('localedir')
pythondir = prefix / python.get_install_dir()

pkgdatadir = datadir / meson.project_name()

appdatadir = datadir / 'metainfo'
applicationsdir = datadir / 'applications'
sleepcoverdir = pythondir / 'sleepcover'
iconsdir = datadir / 'icons'
schemasdir = datadir / 'glib-2.0' / 'schemas'

bin_config = configuration_data()
bin_config.set('localedir', localedir)
bin_config.set('pkgdatadir', pkgdatadir)
bin_config.set('pythondir', pythondir)
bin_config.set('schemasdir', schemasdir)
bin_config.set('app_id', APP_ID)
bin_config.set('base_id', BASE_ID)
bin_config.set('version', meson.project_version())

configure_file(
  input: 'sleep-cover.py.in',
  output: 'sleep-cover',
  configuration: bin_config,
  install_dir: bindir
)

subdir('data')
subdir('sleepcover')
subdir('po')

gnome.post_install(
  glib_compile_schemas: true,
  gtk_update_icon_cache: true,
  update_desktop_database: true
)
