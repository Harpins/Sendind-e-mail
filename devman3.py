import os
from dotenv import load_dotenv
import smtplib
load_dotenv("LoginData.env")
login = os.getenv("login")
password = os.getenv("password")

server=smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)

reference="https://dvmn.org/referrals/eTiqT7jZfQHf52ILYS8RfbngK1gE8HI4wx7SxWuV/"
friend_name="Пророк Санбой"
my_name="Твой Повелитель"
mail="""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
mail=mail.replace("%website%", reference)
mail=mail.replace("%friend_name%", friend_name)
mail=mail.replace("%my_name%", my_name)
receiver="shroom2207@yandex.ru"
subject="Приглашение!"
letter=f"""From: {login}
To: {receiver}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

{mail}"""
letter=letter.encode("UTF-8")

server.sendmail(login, receiver, letter)
server.quit()
