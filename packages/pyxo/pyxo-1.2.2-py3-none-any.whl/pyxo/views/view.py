from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def print(self) -> str | None:
        pass
