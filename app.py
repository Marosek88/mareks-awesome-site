from flask import Flask, render_template, request
import os


APP_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')
STATIC_PATH = os.path.join(APP_PATH, 'static/')
app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/template_page')
def template_page():
	html = request.args.get('html') + '.html'
	return render_template(html)


if __name__ == '__main__':
	app.run()
