# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 20), Item(vest, 10, 20), Item(vest, 5, 20)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(19, items[1].quality)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(19, items[2].quality)


if __name__ == '__main__':
    unittest.main()
