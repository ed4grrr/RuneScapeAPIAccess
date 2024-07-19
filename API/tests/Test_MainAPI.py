import unittest

from API.scripts._MainAPI import _API as API


class _MainAPITestCase(unittest.TestCase):

    def setUp(self):
        self.mainAPItest = API()

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
