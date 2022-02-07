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

import sys
import gi

from gi.repository import Gtk, Gio, Adw

from .window import SleepcoverWindow, AboutDialog


class Application(Adw.Application):
    def __init__(self,version,application_id):
        super().__init__(application_id=application_id,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self_version = version

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = SleepcoverWindow(application=self)
            if self.props.application_id.endswith('Devel'):
                win.get_style_context().add_class('devel')
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        win.present()

    def on_about_action(self, widget, _):
        about = AboutDialog(self.props.active_window)
        about.present()

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')

    def create_action(self, name, callback):
        """ Add an Action and connect to a callback """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)