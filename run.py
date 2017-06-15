# encoding: utf-8
from flask import render_template
from appmanage import create_app

app = create_app()


@app.route('/api_test/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
