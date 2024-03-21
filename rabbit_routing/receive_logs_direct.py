import sys  # Импорт модуля sys для работы с аргументами командной строки
import pika  # Импорт модуля pika для работы с RabbitMQ

connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))  # Установка соединения с сервером RabbitMQ
channel = connection.channel()  # Создание канала связи с сервером

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')  # Объявление прямого обмена под названием 'direct_logs'

result = channel.queue_declare(queue='', exclusive=True)  # Объявление очереди без указания имени, сделано для получения случайного имени очереди
queue_name = result.method.queue  # Получение имени созданной очереди

severities = sys.argv[1:]  # Извлечение уровней важности из аргументов командной строки
if not severities:  # Проверка наличия указанных уровней важности
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])  # Вывод сообщения об использовании, если уровни важности не указаны
    sys.exit(1)  # Завершение программы с ошибкой

for severity in severities:  # Цикл по всем указанным уровням важности
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)  # Привязка очереди к обмену для каждого уровня важности

print(' [*] Waiting for logs. To exit press CTRL+C')  # Вывод сообщения ожидания получения сообщений

def callback(ch, method, properties, body):  # Определение функции обратного вызова для обработки полученных сообщений
    print(f" [x] {method.routing_key}:{body}")  # Вывод полученного сообщения с указанием уровня важности

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)  # Начало потребления сообщений из очереди с указанием функции обратного вызова и автоматического подтверждения получения

channel.start_consuming()  # Запуск процесса получения сообщений