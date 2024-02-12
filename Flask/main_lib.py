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
    proflist = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                        'инженер по терраформированию', 'климатолог',
                        'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                        'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                        'штурман', 'пилот дронов']
    return render_template('list_prof.html', types=types, proflist=proflist)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
