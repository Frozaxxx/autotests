# DemoQA UI autotests

Учебный проект на Python, pytest и Selenium. Первый тест заполняет имя и email в форме [Text Box](https://demoqa.com/text-box), отправляет форму и проверяет оба значения в блоке результата.

## Запуск в PyCharm

1. Открой папку проекта через **File → Open**.
2. Выбери интерпретатор Python 3.11 или новее и создай окружение в папке `.venv`.
3. Убедись, что установлен Google Chrome.
4. В терминале PyCharm из корня проекта выполни:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
```

Для первого запуска нужен интернет. Selenium Manager автоматически подбирает и при необходимости скачивает ChromeDriver.

В `tests/conftest.py` фикстура `browser` открывает Chrome перед тестом и закрывает его после проверки. В `tests/test_text_box.py` находится сам сценарий.
