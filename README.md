# Бот для ведения диалогов с пользователями во Вконтакте или Telegram

Состоит из двух независимых ботов для:
- Telegram
- VK

Создание диалогов происходит через сервис [Dialogflow](https://dialogflow.cloud.google.com/)

## Перед использованием

- Создайте проект в [GoogleCloud](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.102882952.945628098.1664273348-1333030587.1663324445) и получите его id
- Зайдите под тем же гугл-аккаунтом в [Dialogflow](https://dialogflow.cloud.google.com/) и создайте агента, выбрав предварительно созданный проект
- Подключите API вашего проекта по [ссылке](https://console.cloud.google.com/flows/enableapi?apiid=dialogflow.googleapis.com&_ga=2.235976969.945628098.1664273348-1333030587.1663324445)
- Скачайте и установите [GCloudCLI](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe)
- В командной строке введите `gcloud auth application-default login`
- Если выдало предупреждение, то `gcloud auth application-default set-quota-project ID_проекта`

Для работы Telegram бота получите его токен [(Как создать канал, бота и получить токен.)](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) 

Для работы ВК бота создайте группу и получите ключ API для работы с сообщениями сообщества.
## Как установить

В папке со скриптом необходимо создать файл `.env` и записать в него настройки в виде:
```
PROJECT_ID=id проекта Dialogflow/GoogleCloud
TG_TOKEN=токен телеграм бота
VK_API_TOKEN=токен API группы ВК
```

[Python 3.7+](https://www.python.org/downloads/) должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Запуск и использование

Создайте и заполните intent'ы агента в Dialogflow или же используйте команду `python dialog_flow.py --json_path demo_intents.json` для того чтобы загрузить тестовые данные в DF. Вы также можете создать свой собственный JSON файл с вопросами и ответами и использовать его вместо `demo_intents.json` 

Для запуска Telegram бота необходимо ввести команду:
```
python telegram_bot.py
```
Для запуска ВК бота необходимо ввести команду:
```
python vk_bot.py
```

### Альтернативный вариант запуска(Только для ОС Windows):

Запустить один из файлов:
- `tg_bot.bat` - для запуска Telegram бота
- `vk_bot.bat` - для запуска ВК бота

Также Вы можете добавить данный файл в автозагрузку для того чтобы бот запускался при запуске ПК.

Для этого:
- Создайте ярлык нужного вам `.bat` файла, нажав на него правой кнопкой мыши и выбрав пункт "Создать ярлык"
- Нажмите клавишу с логотипом Windows + R, напечатайте shell:startup, затем нажмите ОК. Откроется папка Автозагрузка.
- Скопируйте и вставьте ярлык в папку автозагрузки

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).