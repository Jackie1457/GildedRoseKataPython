import unittest

from gilded_rose import Item, GildedRose

def test_sulfuras_never_changes(self):
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEqual(0, items[0].sell_in, "SellIn should not change for Sulfuras")
    self.assertEqual(80, items[0].quality, "Quality should not change for Sulfuras")

if __name__ == '__main__':
    unittest.main()