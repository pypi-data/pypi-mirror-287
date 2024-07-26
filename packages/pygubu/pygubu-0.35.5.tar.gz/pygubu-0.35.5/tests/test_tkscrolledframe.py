# encoding: utf-8
import os
import sys
import unittest
import tkinter as tk
import tkinter.ttk as ttk


import fixpath
import pygubu
import support
from pygubu.widgets.tkscrolledframe import TkScrolledFrame


class TestTtkScrolledframe(unittest.TestCase):
    def setUp(self):
        support.root_deiconify()
        xmldata = "test_tkscrolledframe.ui"
        self.builder = builder = pygubu.Builder()
        builder.add_from_file(xmldata)
        self.widget = builder.get_object("scrolledframe")

    def tearDown(self):
        support.root_withdraw()

    def test_class(self):
        self.assertIsInstance(self.widget, TkScrolledFrame)
        self.widget.destroy()
