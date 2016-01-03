#!/usr/bin/env python
from gi.repository import Gtk
from PlayExt import *

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

    def addone(self):
        """ add_link refers to the button to add new entry box for links"""
        
        top_box = Gtk.Grid()
        self.page1.add(top_box)
        
        ex_label = Gtk.Label("Enter Links: ")
        self.link_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        add_link = Gtk.Button(label="+Add link")
        button = Gtk.Button(label="Start Download")

        add_link.connect("clicked", self.click_add_link)
        button.connect("clicked", self.click_links)
        self.links = []
        self.click_add_link()

        top_box.attach(ex_label, 0, 0, 1, 1)
        top_box.attach(self.link_box, 1, 0, 1, 1)
        top_box.attach(add_link, 2, 0, 1, 1)
        top_box.attach(button, 0, 1, 3, 1)

    def addtwo(self):
        top_box = Gtk.Grid()
        self.page2.add(top_box)

        ex_label = Gtk.Label("Playlist URL: ")
        self.play_entry = Gtk.Entry()
        button = Gtk.Button(label="Start Download")
        button.connect("clicked", self.click_playlist)

        top_box.attach(ex_label, 0, 0, 1, 1)
        top_box.attach(self.play_entry, 1, 0, 1, 1)
        top_box.attach(button, 0, 1, 2, 1)

    def click_playlist(self, button):
        play_link = self.play_entry.get_text()
        get_playlist(play_link)
        
        #print("Playlist Download")

    def click_add_link(self, button=None):
        self.links.append(Gtk.Entry())
        self.link_box.pack_start(self.links[-1], True, True, 0)
        self.show_all()

        #print("Add links")
        
    def click_links(self, button):
        for x in self.links:
            get_download(x.get_text())

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
