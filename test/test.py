import unittest
import myproject

class MyTest(unittest.TestCase):
  def test_HELLO(self):
    self.assertEqual(myproject.HELLO, 'hello')
