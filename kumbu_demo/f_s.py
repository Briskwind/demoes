from __future__ import absolute_import, unicode_literals

from kombu import Connection, Queue
from kombu import Producer
from kombu.mixins import ConsumerMixin
from kumbu_demo import services

class Server(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        self.producer = Producer(self.connection)
        self.queue = Queue('rpc_queue')

    def get_consumers(self, Consumer, channel):
        return [Consumer(
            queues=[self.queue],
            on_message=self.on_request,
            accept={'application/json'},
        )]

    def on_request(self, message):
        print('message.payload', message.payload)
        fun = message.payload['fun']
        args = message.payload['args']
        kwargs = message.payload['kwargs']

        function = getattr(services, fun)
        result = function(*args, **kwargs)
        print('result', result)

        self.producer.publish(
            {'result': result},
            exchange='', routing_key=message.properties['reply_to'],
            correlation_id=message.properties['correlation_id'],
            serializer='json',
            retry=True,
        )
        message.ack()


def start_worker(broker_url):
    connection = Connection(broker_url)
    print(' [x] Awaiting RPC requests')
    worker = Server(connection)
    worker.run()


if __name__ == '__main__':
    try:
        start_worker('amqp://guest:guest@localhost:5672//')
    except KeyboardInterrupt:
        pass