# main.py
#
# Copyright 2022 Aurnytoraink
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gettext import gettext as _
from gi.repository import Gtk, Gio, Adw, GObject, GLib

from sleepcover.ui.window import SleepcoverWindow
from sleepcover.ui.aboutdialog import AboutDialog


class Application(Adw.Application):

    settings = GObject.Property(type=Gio.Settings)
    version = GObject.Property(type=str)

    def __init__(self,application_id,version):
        super().__init__(application_id=application_id,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.name = _("SleepCover")
        self.version = version
        self.settings = Gio.Settings.new(self.get_application_id())
        GLib.set_application_name(self.name)
        GLib.set_prgname("sleepcover")
        Gtk.Window.set_default_icon_name(self.get_application_id())


    def do_activate(self):
        self.win = self.props.active_window
        if not self.win:
            self.win = SleepcoverWindow(application=self)
            if self.props.application_id.endswith('Devel'):
                self.win.get_style_context().add_class('devel')
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        self.win.present()

    def do_startup(self):
        Adw.Application.do_startup(self)

    def on_preferences_action(self, widget, *param):
        print('app.preferences action activated')

    def on_about_action(self, widget, *param):
        about = AboutDialog(self.win, self.version, self.get_application_id())
        about.present()

    def create_action(self, name, callback):
        """ Add an Action and connect to a callback """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
