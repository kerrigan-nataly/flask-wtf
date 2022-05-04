import os
from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if prof in ['инженер', 'строитель']:
        sim = "Инженерные тренажеры"
        img = 'ship.jpg'
    elif prof in ['врач', 'гляциолог', 'астрогеолог', 'климатолог', 'экзобиолог']:
        sim = "Научные симуляторы"
        img = 'ship-s.jpg'
    else:
        img = "ship-wtf.jpg"
        sim = "Вы кто? Пройдите в криокамеру"

    return render_template('training.html', img_name=img, sim=sim)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', profs=[
        'инжинер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терраформированию',
        'климатолог',
        'специалист по радиозащите',
        'астрогеолог',
        'гляциолог',
        'инженер жизнеобеспечения',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов'
    ], list=list)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    fields = {
        'title': 'Анкета',
        'surname': 'Wanty',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', fields=fields)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/distribution')
def distribution():
    astronauts = [
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тэдди Сандерс',
        'Шон Бин'
    ]
    return render_template('distribution.html', astronauts=astronauts)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if sex == 'male':
        wall_color = 'red'
    else:
        wall_color = 'blue'

    if age >= 21:
        poster = "old.jpg"
    else:
        poster = "young.png"

    return render_template('table.html', wall_color=wall_color, poster=poster)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    imgdir = '/'.join([app.static_folder, 'img', 'galery'])
    if request.method == 'GET':
        images = os.listdir(imgdir)
        # C:\Users\Nat\Documents\GitHub\flask-wtf\static/img/galery
        return render_template('galery.html', images=images)

    elif request.method == 'POST':

        f = request.files.get('file')

        if not f:
            return "Не выбран файл"

        f.save('/'.join([imgdir, f.filename]))
        return redirect('/galery')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
