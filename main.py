from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!<br>
            Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                     <h1>Жди нас, Марс!</h1>
                     <img src="{url_for('static', filename='img/mars.jpg')}" width=500 height=400 
                     alt="здесь должна была быть картинка, но не нашлась">
                     <p>Вот она какая, красная планета.</p>
                </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Колонизация</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                     <h1>Жди нас, Марс!</h1>
                     <img src="{url_for('static', filename='img/mars.jpg')}" width=500 height=400 
                     alt="здесь должна была быть картинка, но не нашлась">
                     <p color=#ffff00>Человечество вырастает из детства.</p>
                     <p>Человечеству мала одна планета.</p>
                     <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                     <p>И начнем с Марса!</p>
                     <p>Присоединяйся!</p>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
