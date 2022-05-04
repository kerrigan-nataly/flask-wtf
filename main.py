from flask import Flask
from flask import render_template

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
