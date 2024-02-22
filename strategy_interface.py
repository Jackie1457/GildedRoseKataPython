from abc import ABC, abstractmethod

class UpdateStrategy(ABC):
    @abstractmethod
    def update(self, item):
        pass
