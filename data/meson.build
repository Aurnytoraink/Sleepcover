gnome.compile_resources(
  BASE_ID,
  BASE_ID + '.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

desktop_conf = configuration_data()
desktop_conf.set('application_id', APP_ID)

# Merging the translations with the desktop file
desktop_conf = configuration_data()
desktop_conf.set('icon', APP_ID)
i18n.merge_file(
  type: 'desktop',
  input: configure_file(
    output: BASE_ID + '.desktop.in',
    input: BASE_ID + '.desktop.in.in',
    configuration: desktop_conf),
  output: APP_ID + '.desktop',
  po_dir: meson.project_source_root() / 'po',
  install: true,
  install_dir: applicationsdir
)

# Validating the desktop file
desktop_file_validate = find_program('desktop-file-validate', required:false)
if desktop_file_validate.found()
  test (
    'Validate desktop file',
    desktop_file_validate,
    args: join_paths(meson.current_build_dir (), APP_ID + '.desktop')
  )
endif


appstream_conf = configuration_data()
appstream_conf.set('APP_ID', APP_ID)
appstream_file = i18n.merge_file(
  input: configure_file(
    input: 'com.github.Aurnytoraink.Sleepcover.metainfo.xml.in.in',
    output: '@BASENAME@',
    configuration: appstream_conf
  ),
  output: '@0@.metainfo.xml'.format(APP_ID),
  po_dir: 'meson.project_source_root()' / 'po',
  install: true,
  install_dir: appdatadir
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

gsettings_conf = configuration_data()
gsettings_conf.set('application_id', APP_ID)
configure_file(
  input: 'com.github.Aurnytoraink.Sleepcover.gschema.xml.in',
  output: '@0@.gschema.xml'.format(APP_ID),
  configuration: gsettings_conf,
  install: true,
  install_dir: schemasdir
)


compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas,
    args: ['--strict', '--dry-run', meson.current_source_dir()]
  )
endif

install_subdir('icons/hicolor', install_dir: iconsdir)
