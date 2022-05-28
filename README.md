<h2 align="center">FullStatsNet by Django</h2>


### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=django-insecure-7^w*bsr$yp^uv)vf48wql%dw_&gu^8z9h%_=njune@isgj9#0d
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=pysonet
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=pysonet
    POSTGRES_USER=pysonet_user
    POSTGRES_PASSWORD=pysonet_pass
    POSTGRES_HOST=pysonet-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec -it pysonet_pysonet_back_1 python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
 
## License

Copyright (c) 2022-present, Gorban Alexander




