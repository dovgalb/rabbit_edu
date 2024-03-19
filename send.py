import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером
connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))

# Создаем канал для обмена данными с брокером
channel = connection.channel()

# Объявляем очередь с именем 'hello', если такая очередь еще не существует
channel.queue_declare(queue='hello')

# Цикл, который будет повторяться 100 раз
for i in range(1):
    # Публикуем сообщение с текстом 'Hello World!' в очередь 'hello'
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    count_cycles = i + 1


print(f"[x] Sent 'Hello World!' [{count_cycles} times]")  # Выводим сообщение об отправке сообщения в консоль

connection.close()  # Закрываем соединение с брокером RabbitMQ после отправки сообщений
