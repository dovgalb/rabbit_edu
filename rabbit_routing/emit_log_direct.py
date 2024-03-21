import sys  # Импорт модуля sys для работы с аргументами командной строки

import pika  # Импорт модуля pika для работы с RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))  # Установка соединения с сервером RabbitMQ

channel = connection.channel()  # Создание канала связи с сервером

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')  # Объявление прямого обмена под названием 'direct_logs'

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'  # Извлечение уровня важности из аргументов командной строки или использование 'info' по умолчанию
message = ' '.join(sys.argv[2:]) or 'Hello World!'  # Формирование сообщения из аргументов командной строки или использование 'Hello World!' по умолчанию
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)  # Отправка сообщения с указанным уровнем важности и содержанием
print(f" [x] Sent {severity}:{message}")  # Вывод подтверждения отправки сообщения
connection.close()  # Закрытие соединения