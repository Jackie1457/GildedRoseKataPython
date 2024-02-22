import unittest

from gilded_rose import Item, GildedRose

class AgedBrieTest(unittest.TestCase):
    def test_aged_brie_increases_in_quality_over_time(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in, "SellIn should decrease by 1")
        self.assertEqual(1, items[0].quality, "Quality should increase by 1 as Aged Brie gets older")

if __name__ == '__main__':
    unittest.main()