import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.form:
		print(request.form)
	return render_template('index.html')


@app.route('/result',methods=['POST'])
def stockresults():

    # Read user input from form
    tickersymbol = request.form['tickersymbol']
    return render_template('result.html')

if __name__ == '__main__':
	app.run(debug=True)