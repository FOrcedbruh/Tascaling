from app.utils.broker.base import BaseBrokerClient
from aiokafka import AIOKafkaProducer
from app.core.settings import get_settings
import json

settings = get_settings()


class KafkaClient(BaseBrokerClient):

    @classmethod
    def get_producer(cls) -> AIOKafkaProducer:
        return AIOKafkaProducer(
            bootstrap_servers=settings.kafka.server
        )
    
    @classmethod
    async def produce_one(cls, producer: AIOKafkaProducer, topic: str, value: bytes):
        await producer.start()
        try:
            await producer.send_and_wait(topic=topic, value=value)
        except Exception as e:
            raise e
        finally:
            await producer.stop()
        
    @classmethod
    async def produce_mail(cls, producer: AIOKafkaProducer, mail_data: dict):
        return await cls.produce_one(producer, topic=settings.kafka.mail_topic, value=json.dumps(mail_data).encode())