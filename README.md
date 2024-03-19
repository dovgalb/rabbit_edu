# Установить виртуальное окружение
`pyenv install 3.11.5
`

`pyenv local 3.11.5`

`python -m venv venv`

`source venv/bin/activate`

# Установить и запусть брокер
`cd slarm_stand3`

`docker compose up -d`

docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p 15672:15672 -p 5672:5672 rabbitmq

