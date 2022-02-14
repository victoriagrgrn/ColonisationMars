from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <br>Вот она какая, красная планета.
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.jpg')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-dark" role="alert">
                            Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-secondary" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                            Присоединяйся!
                            </div>
                          </body>
                        </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                            <title>Отбор Астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center" >Анкета претендента</h1>
                            <h2 align="center" >на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="fname" placeholder="Введите имя" name="fname">
                                    <input type="text" class="form-control" id="lname" placeholder="Введите фамилию" name="lname">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <br> Какие у вас есть профессии?
                                     <div class="form-group">
                                        <input type="checkbox" id="vehicle1" name="engineer">
                                        <label for="engineer"> инженер-исследователь</label><br>
                                        <input type="checkbox" id="vehicle1" name="pilot">
                                        <label for="pilot"> пилот</label><br>
                                        <input type="checkbox" id="vehicle1" name="builder">
                                        <label for="builder"> строитель</label><br>
                                        <input type="checkbox" id="vehicle1" name="biologist">
                                        <label for="biologist"> экзобиолог</label><br>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите приянть участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['fname'])
        print(request.form['lname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['about'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
