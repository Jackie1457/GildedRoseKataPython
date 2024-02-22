import unittest
from gilded_rose import Item, GildedRose

class BackstagePassesTest(unittest.TestCase):
    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in, "SellIn should decrease by 1")
        self.assertEqual(21, items[0].quality, "Quality should increase by 1 when there are more than 10 days")

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose([items[0]])
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality, "Quality should increase by 2 when there are 10 or less days")

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose([items[0]])
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality, "Quality should increase by 3 when there are 5 or less days")

if __name__ == '__main__':
    unittest.main()
