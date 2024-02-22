from strategy_interface import UpdateStrategy

class BackstagePassesStrategy(UpdateStrategy):
    def update(self, item):
        if item.sell_in > 10:
            increment = 1
        elif item.sell_in > 5:
            increment = 2
        else:
            increment = 3

        item.quality = min(50, item.quality + increment)

        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0