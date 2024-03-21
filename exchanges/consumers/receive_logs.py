import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером
connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))

# Создаем канал для обмена данными с брокером
channel = connection.channel()

# объявляем обменник с именем 'logs' и типом 'fanout'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Объявляем очередь с именем 'hello', если такая очередь еще не существует
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# объявляем привязку очереди к обменнику
channel.queue_bind(exchange='logs', queue=queue_name)

# Выводим сообщение об отправке сообщения в консоль
print(' [*] Waiting for logs. To exit press CTRL+C')


# Функция обратного вызова, которая будет вызываться при получении сообщения
def callback(ch, method, properties, body):
    # with open('logs_from_rabbit.log', 'a') as file:
    #     file.write(f"{body}\n")
    print(f" [x] {body}")

# Запускаем обработчик сообщений
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True
)

# Начинаем прослушивание (ожидание) сообщений в очереди
channel.start_consuming()