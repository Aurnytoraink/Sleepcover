about_dialog_conf = configuration_data()
about_dialog_conf.set('version', meson.project_version())
about_dialog_conf.set('app_id', APP_ID)

about_dialog = configure_file(
  input: 'about-dialog.ui.in',
  output: 'about-dialog.ui',
  configuration: about_dialog_conf,
)
