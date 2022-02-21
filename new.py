import datetime

from flask import Flask
from data import db_session
from data.news import News
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #user = User()
    #user.name = "Пользователь 3"
    #user.about = "биография пользователя 3"
    #user.email = "email3@email.ru"
    db_sess = db_session.create_session()
    #db_sess.add(user)
    #db_sess.commit()

    user = db_sess.query(User).first()
    print(user.name)

    for user in db_sess.query(User).filter(User.id > 1,
                                           User.email.notilike("%1%")):
        print(user)

    # user = db_sess.query(User).filter(User.id == 1).first()
    # print(user)
    # user.name = "Измененное имя пользователя"
    # user.created_date = datetime.datetime.now()
    # db_sess.commit()

    # db_sess.query(User).filter(User.id >= 3).delete()
    # db_sess.commit()
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()

    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()

