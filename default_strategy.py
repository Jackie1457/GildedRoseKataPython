from strategy_interface import UpdateStrategy

class DefaultStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
