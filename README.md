# Skillbox Market

### About
Данный проект был разработан на Django. Главная задача - создание платформы интернет-магазина с полной функциональностью такими как: просмотр и редактирование администратором товаров, заказов, категорий каталогов и тд.; наличие личного кабинета у пользователя; показ товаров с фильтрами, а также их сравнение; оформление заказов.

### Code style

В проекте используется [ruff](https://docs.astral.sh/ruff/) библиотека.

Подробнее про правила (rules) и настройки (settings) можно прочитать в документации:

- [rules](https://docs.astral.sh/ruff/rules/)
- [settings](https://docs.astral.sh/ruff/settings/)

### Project variables

Все нужные переменные хранятся в файле `.env.example`, который следует скопировать в корень проекта.

Для macOS и Linux:

```bash
cp .env.example .env
```

Для Windows:

```bash
copy .env.example .env
```

### PostgreSQL settings

1. Установить [PostgerSQL](https://www.postgresql.org/download/) локально
2. Запустить и выполнить следующие команды:

``` SQL
CREATE DATABASE db_name;
CREATE ROLE user with password 'password';
ALTER ROLE "user" WITH LOGIN;
GRANT ALL PRIVILEGES ON DATABASE "db_name" to user;
ALTER USER user CREATEDB;
```

где `db_name` - название базы данных, `user` - имя пользователя, `password` - пароль пользователя

После создания БД и пользователя, необходимо указать их в файле `.env` в виде строки подключения к БД:

```
DATABASE_URL=postgres://user:password@host:port/db_name
```

### Celery settings

1. Установить и запустить [Redis](https://redis.io/download) локально
2. Запустить Celery в отдельном терминале: ```celery -A marketplace worker -l INFO```
3. Запустить Celery Beat в отдельном терминале: ```celery -A marketplace beat```

Для создания периодической задачи для обновления продукта "Предложение дня" необходимо запустить команду:

```bash
./manage.py create_periodic_task_for_daily_product
```

### Documentation
#### Orders
- admin.py
  - OrderAdmin - регистрация модели Order в административной панели
  - OrderItemInline - детализация сущности в административной панели
- cart.py
  - Cart - модель корзины для товаров
    - add - добавление товара в корзину
    - remove - удаление товара из корзины
    - get_total_price - получение полной стоимости корзины
    - get_total_discount_price - получение стоимости корзины со скидками на товары
    - get_total_original_price - получение стоимости корзины на товары с ценами без скидки
    - get_cart_price_with_discount - получение стоимости корзины со скидкой на корзину
    - get_difference_original_price_and_discount_price - получение разницы оригинальной скидочной цены на товар
- forms.py
  - OrderCreateForm - форма оформления заказа
- models.py
  - Order - модель заказов
  - OrderItem - модель деталей заказов
- views.py
  - cart_add - добавление товаров в корзину
  - cart_remove - удаление товара из корзины
  - CartTemplateView - модель отображения страницы с корзиной
  - OrderCreateView - модель создания заказа
  - OrderDetailView - модель детализации заказов

