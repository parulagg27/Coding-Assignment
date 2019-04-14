import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import SearchForm
#from models import Stocks

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "stocksdatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'
db = SQLAlchemy(app)


class Stocks(db.Model):
	stock_symbol = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
	#stock_name = db.Column(db.String(120), unique=True, nullable=False)
	stock_price = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return '<Stock Price for {}: {}>'.format(self.stock_symbol, self.stock_price)
		

@app.route('/', methods=['GET', 'POST'])
def main():
	form = SearchForm()
	if form.validate_on_submit():
		return redirect(url_for('result'))
	return render_template('index.html', form=form)


@app.route('/result',methods=['POST'])
def stockresults():

    # Read user input from form
	tickersymbol = request.form['tickersymbol']
	stocksymbol = Stocks.query.filter_by(stock_symbol=tickersymbol)
  
	return render_template('result.html', tickersymbol=tickersymbol, stocksymbol=stocksymbol)

if __name__ == '__main__':
	app.run(debug=True)