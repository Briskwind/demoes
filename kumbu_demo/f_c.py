from __future__ import absolute_import, unicode_literals

from kombu import Connection, Producer, Consumer, Queue, uuid


class KombuRpcClient(object):
    def __init__(self, connection):
        self.connection = connection
        self.callback_queue = Queue(uuid(), exclusive=True, auto_delete=True)
        self.response = None
        self.correlation_id = uuid()

    def on_response(self, message):
        """ 接受服务器的响应"""
        if message.properties['correlation_id'] == self.correlation_id:
            self.response = message.payload['result']

    def send_request(self, fun, args, kwargs):
        payload = {'fun': fun, 'args': args, 'kwargs': kwargs}

        with Producer(self.connection) as producer:
            producer.publish(
                payload,
                exchange='',
                routing_key='rpc_queue',
                declare=[self.callback_queue],
                reply_to=self.callback_queue.name,
                correlation_id=self.correlation_id,
            )

        # 接受服务器发布的消息, 接受到后进入 on_response 回调
        with Consumer(self.connection,
                      on_message=self.on_response,
                      queues=[self.callback_queue], no_ack=True):
            while self.response is None:
                self.connection.drain_events()
        return self.response


def main(broker_url):
    connection = Connection(broker_url)
    rpc_client = KombuRpcClient(connection)
    print(' [x] Requesting fib(30)')
    parameter = {'fun': 'fib', 'args': (30,), 'kwargs': {}}

    response = rpc_client.send_request(**parameter)
    print(' [.] Got {0!r}'.format(response))


if __name__ == '__main__':
    main('amqp://guest:guest@localhost:5672//')
