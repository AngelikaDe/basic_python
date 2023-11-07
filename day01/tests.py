import unittest
from ex00 import add_ingot, get_ingot, empty
from ex01 import split_booty


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
    def test_split_booty(self):
        res = split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10})
        self.assertEqual(res, [{"gold_ingots": 3}, {"gold_ingots":3}, {"gold_ingots": 2}])
        res = split_booty({"gold_ingots": 0}, {"gold_ingots": 0}, {"apples": 10})
        self.assertEqual(res, [{'gold_ingots': 0}, {'gold_ingots': 0}, {'gold_ingots': 1}])

if __name__ == '__main__':
    unittest.main()
