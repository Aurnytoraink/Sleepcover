subdir('icons')

gnome = import('gnome')

gnome.compile_resources('sleepcover',
  'sleepcover.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

desktop_conf = configuration_data()
desktop_conf.set('application_id', application_id)

desktop_file = i18n.merge_file (
  type: 'desktop',
  input: configure_file(
    input: 'com.github.Aurnytoraink.Sleepcover.desktop.in.in',
    output: '@BASENAME@',
    configuration: desktop_conf
  ),
  output: '@0@.desktop'.format(application_id),
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)


desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

appstream_conf = configuration_data()
appstream_conf.set('APP_ID', application_id)
appstream_file = i18n.merge_file(
  input: configure_file(
    input: 'com.github.Aurnytoraink.Sleepcover.metainfo.xml.in.in',
    output: '@BASENAME@',
    configuration: appstream_conf
  ),
  output: '@0@.metainfo.xml'.format(application_id),
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'metainfo')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

gsettings_conf = configuration_data()
gsettings_conf.set('application_id', application_id)
configure_file(
  input: 'com.github.Aurnytoraink.Sleepcover.gschema.xml.in',
  output: '@0@.gschema.xml'.format(application_id),
  configuration: gsettings_conf,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)


compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas,
    args: ['--strict', '--dry-run', meson.current_source_dir()]
  )
endif
