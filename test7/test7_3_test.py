import unittest

from test7.test7_3 import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print('before...')

    def tearDown(self):
        print('after...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 调用d['key']期待抛出KeyError异常，
            value = d['key']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):  # 调用d['key']期待抛出AttributeError异常，
            value = d.key


if __name__ == '__main__':  # 运行该.py文件里所有的test
    unittest.main()
