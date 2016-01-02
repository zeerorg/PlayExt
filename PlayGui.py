#!/usr/bin/env python
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PlayExt")

        # For adding tabs support (StackSwitcher looks lame)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # First Page
        self.page1 = Gtk.Box()
        self.addone()                # To create my page layout
        self.notebook.append_page(self.page1, Gtk.Label("Link"))

        # Second Page
        self.page2 = Gtk.Box()
        self.addtwo()               # To create my second page layout
        self.notebook.append_page(self.page2, Gtk.Label("Playlist"))
        
        self.set_border_width(10)
        self.set_default_size(500, 400)

    def addone(self):
        top_box = Gtk.Box()
        self.page1.add(top_box)
        top_box.add(Gtk.Label("Enter Links: "))

    def addtwo(self):
        top_box = Gtk.Box()
        self.page2.add(top_box)
        top_box.add(Gtk.Label("Playlist URL: "))



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
