from flask import Flask, render_template

app = Flask('My first site')


@app.route('/')
def start_jo():
    return 'Привіт, дрhhhуже'


@app.route('/list')
def list_ul():
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    return render_template('list.html', title='List', k=k)


@app.route('/show/<int:number>')
def show_number(number):
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    return render_template('show_number.html', title='Show number', number=number, k=k)


@app.route('/filter/<word>')
def filter_word(word):
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    return render_template('filter_word.html', title='Filter word', word=word, k=k)


if __name__ == '__main__':
    app.run()
