# -*- coding: utf-8 -*-
from aged_brie_strategy import AgedBrieStrategy
from sulfur_as_strategy import SulfurasStrategy
from backstage_passes_strategy import BackstagePassesStrategy
from default_strategy import DefaultStrategy
from typing import List

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: List[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.strategy_map = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategy_map.get(item.name, DefaultStrategy())
            strategy.update(item)
