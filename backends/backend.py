from abc import abstractmethod, ABC


class Backend(ABC):
    @abstractmethod
    def write(self, status):
        pass
