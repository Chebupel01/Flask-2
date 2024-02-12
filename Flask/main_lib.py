from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<types>')
def list_prof(types):
    a = 1
    proflist = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                'инженер по терраформированию', 'климатолог',
                'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                'штурман', 'пилот дронов']
    return render_template('list_prof.html', types=types, proflist=proflist)


@app.route('/answer')
@app.route('/auto_answer')
def answers():
    data = {'title': 'Анкета', 'surname': 'Васильев', 'name': 'Дима', 'education': 'Высшее', 'profession': 'Космонавт',
            'sex':
                'Мужской', 'motivation': 'Всегда мечтал покушать картошки с марса', 'ready': 'Готов'}
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
