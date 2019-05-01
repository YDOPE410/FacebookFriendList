import abc

class Config_loader(abc.ABC):

    @abc.abstractmethod
    def load(path):
        pass

    @abc.abstractmethod
    def _verify(config):
        pass