# ELEMENTARY 

## An Gaming Platform for Institutions to organize gaming events.


![main1](https://user-images.githubusercontent.com/28597524/99024925-a859b580-258d-11eb-8f9a-1b944e36b209.jpg "ELEMENTARY")

See installation [here](#how-to-install)

## What is this?
ELEMENTARY is a AI based gaming platform designed for Instiution Level Gaming Contest with support upto 1 Million Players.
Users can easily login and play levels with AI base Ranking system and in-game music support.
Custom Admin Panel to track user activity(including SQL Injection) and to add levels and use notifications service.
Social media platform for users to search other players and check stats.
Each Level has it own comment thread to discuss with each other just in case if your stuck.
Unbeatable protection against cheaters and hackers.
FB, Google+ and GitHuB Social Logi support.
Developed on Django.


## Features
- User Friendly Platform
- Notifications enabled  
- User activity report
- Analytics
- Leaderboard
- Accurate Ranking Algorithm
- Admin Panel to add levels
- In Game Music
- WebGL enabled
- Customized Profile
- Search other players
- Ddos protection
- Anti Cheat
- much more

![main2](https://user-images.githubusercontent.com/28597524/99024968-bb6c8580-258d-11eb-933f-c8a35068a8f1.jpg "ELEMENTARY UI")

### Efficient
ELEMENTARY uses the celery worker feature to split the multiple tasksand perform it in a queue.
We can have upto 10 celery workers at a time. This feature allows us maintain a large user base.


## How to Install
- Create virtual environment, then activate it.
- Install all the requirements file, ``` pip install -r requirements.txt```
- If you want to enable Celery then follow the following steps else just run  ```python manage.py runserver``` after migrating the models.
- Setup RabbitMQ server for broker service, ``` docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```
- start your rabbitmq broker service.
- In elementary setting change ```CELERY_BROKER_URL = 'your_rabbitmq_address'```, if your not using the default port for RabbitMQ.
- Run celery worker, ```celery -A elementary worker -l info```
- For first time usage, ```python manage.py migrate``` and create admin ```python manage.py createsuperuser```
- Run ELEMENTARY, ```python manage.py runserver```





