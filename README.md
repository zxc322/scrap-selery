# scrap-selery

### Create .env file ( example vars you can find in `.sample`)

### run app from docker

    docker-compose up --build 

### Run worker

    docker exec -it web python -m celery -A src.tasks.mail_task worker -l INFO
    
### Run celery beat

    docker exec -it web python -m celery -A src.tasks.telegram_task beat -l INFO
    docker exec -it web python -m celery -A src.tasks.telegram_task worker -l INFO

###### for windows `python -m celery -A src.tasks.mail_task worker -l INFO -P eventlet`

### Use app

#### Scrape cars from page 

example request: `http://localhost:8000/page/?page=4` 

###### It inserts all cars from page into database and returns car with highest price on page (sending mail also)

#### Get the most expensive cars from database

example request : `http://localhost:8000/top?limit=5'`

###### Returns top 5 cars

### API Docs `http://localhost:8000/docs`


    

    

