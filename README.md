# 🚴‍♂️ UI-тесты для сервиса «Яндекс.Самокат» — Sprint 6

Этот проект — автотесты пользовательского интерфейса (UI) сервиса «Яндекс.Самокат», выполненные в рамках шестого спринта обучения.

## 📁 Структура проекта

```
Sprint_6/
├── conftest.py                 # Общие фикстуры (в т.ч. драйвер)
├── data/
│   └── order_data.py           # Тестовые данные для заказов
├── pages/
│   ├── base_page.py            # Базовый класс Page Object
│   ├── locators.py             # Локаторы элементов
│   ├── main_page.py            # Page Object главной страницы
│   └── order_page.py           # Page Object страницы заказа
├── tests/
│   ├── test_faq.py             # Тесты блока FAQ
│   ├── test_logo_redirects.py  # Тесты редиректов по логотипам
│   ├── test_order.py           # Тест заказа (верхняя кнопка)
│   └── test_order_from_bottom_button.py  # Тест заказа (нижняя кнопка)
├── allure-report/              # Каталог отчёта Allure (если сохранён)
└── README.md
```

## 🛠️ Технологии

- Python 3.13+
- Selenium WebDriver
- Pytest
- Allure (для отчётности)
- Page Object Model (POM)

## 🚀 Как запустить тесты

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запуск всех тестов:

```bash
pytest
```

3. Запуск с генерацией Allure-результатов:

```bash
pytest --alluredir=allure-results
```

4. Генерация и открытие HTML-отчёта:

```bash
allure serve allure-results
```

## 📌 Описание тестов

- **test_faq.py** — проверка раскрытия ответов на все вопросы FAQ.
- **test_order.py** — позитивный сценарий заказа через верхнюю кнопку.
- **test_order_from_bottom_button.py** — заказ через нижнюю кнопку.
- **test_logo_redirects.py** — переходы по логотипам: Самокат и Яндекс (редиректы).

## 🔗 Полезное

- Официальный сайт: [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/)
- [Документация Allure](https://docs.qameta.io/allure/)

---

📬 **Автор**: Грабовский Денис  
🎓 Проект выполнен в рамках обучения на платформе Яндекс.Практикум
