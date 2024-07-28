from abc import ABC, abstractmethod


class BaseExecutor(ABC):

    @abstractmethod
    def executor(self):
        pass
