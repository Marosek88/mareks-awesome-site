from flask import Flask, render_template
import os


APP_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')
STATIC_PATH = os.path.join(APP_PATH, 'static/')
app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
