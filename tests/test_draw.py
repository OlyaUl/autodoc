import unittest
import test_class
from unittest.mock import ANY, patch, sentinel # test


class mytest(unittest.TestCase):
   def test_upper(self):
       self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
   test = mytest()
   test.test_upper()


'''class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')'''