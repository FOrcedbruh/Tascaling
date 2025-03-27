from abc import ABC, abstractmethod



class BaseBrokerClient(ABC):

    @classmethod
    @abstractmethod
    def get_producer(cls): ... 


    @classmethod
    @abstractmethod
    async def produce_one(cls): ...
