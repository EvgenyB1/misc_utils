'''
Created on Feb 13, 2014

@author: evgeny
'''
import unittest
import t9


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_t9_key_combo(self):
        self.assertEqual(t9.key_combo('a'), '2',
                         "T9 for 'a' is '2'")
        self.assertEqual(t9.key_combo('B'), '22',
                         "T9 for 'B' is '22'")
        self.assertEqual(t9.key_combo('s'), '7777',
                         "T9 for 's' is '7777'")
        self.assertRaises(ValueError, t9.key_combo, 'aa')

    def test_t9_string(self):
        self.assertEqual(t9.string('foo  bar'), '333666 6660 022 2777',
                         "T9 for 'foo  bar' is 333666 6660 022 2777")
        self.assertEqual(t9.string('a a'), '202',
                         "T9 for 'a a' is 202")
        self.assertEqual(t9.string('a'), '2',
                         "T9 for 'a a' is 2")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
