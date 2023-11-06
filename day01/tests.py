import unittest
from ex00 import add_ingot, get_ingot, empty


class TestEx00(unittest.TestCase):
    def test_add_get_empty(self):
        purse = {}
        res = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(res.get("gold_ingots"), 1)

    def test_add_get(self):
        purse = {'gold_ingots': 10}
        res = add_ingot(get_ingot(add_ingot(purse)))
        self.assertEqual(res.get("gold_ingots"), 11)

class TestEx01(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
