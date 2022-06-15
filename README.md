# Клонирование репозитория

```bash
git clone https://github.com/tyrkinn/raspberry_web_led
```

# Сборка схемы

Схема будет похожа на эту, только в моем случае красный провод подключен к 7 порту, а черный к 6

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdlnmh9ip6v2uc.cloudfront.net%2Fassets%2Fe%2F1%2F4%2Fc%2Fa%2F528bd59d757b7f65548b4567.png&f=1&nofb=1" />

# Установка зависимостей

Установка uvicorn
```bash
sudo apt install uvicorn
```

Установка fastapi
```bash
pip install fastapi
```

# Запуск сервера

## Получение адреса raspberry pi в вашей локальной сети

```bash
hostname -I

# Получаю 192.168.43.253 2a00:1fa0:48c4:39dc:870a:fdf5:8923:a69
# В моем случае адрес - 192.168.43.253
```

## Запуск с помощью скрипта

Сначала нужно изменить хост в скрипте.
Откройте файл start_server.sh и вставьте полученный в предыдущем шаге адрес после флага --host

```bash
sh start_server.sh
```

## Запуск вручную

```bash
sudo uvicorn server:app --port ВАШ_ПОРТ --host ВАШ_ХОСТ
```

## Проверяем работоспособность

С любого устройства в той же локальной сети открываем адрес который будет отображен в терминале после запуска сервера. По корневому роуту должна будет отобразиться кнопка
