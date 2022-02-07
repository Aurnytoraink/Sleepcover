project('sleepcover',
          version: '0.1.0',
    meson_version: '>= 0.50.0',
  default_options: [ 'warning_level=2',
                   ],
)

dependency('gtk4', version: '>= 4.5.0')
dependency('libadwaita-1', version: '>=1.0.0')

pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

i18n = import('i18n')

if get_option('profile') == 'development'
  profile = 'Devel'
else
  profile = ''
endif
application_id = 'com.github.Aurnytoraink.Sleepcover@0@'.format(profile)
base_id = 'com.github.Aurnytoraink.Sleepcover'

subdir('data')
subdir('src')
subdir('po')

meson.add_install_script('build-aux/meson/postinstall.py')
