from flask import Flask, render_template, request
from paydatesidea import payTime
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    start_date = str(request.form['start_date'])
    end_date = str(request.form['end_date'])
    convention = str(request.form['convention'])
    period = str(request.form['period'])
    data = payTime(start_date, end_date, convention, period, 'string')

    return render_template('index.html', data=data,
                           start_date=start_date, end_date=end_date,
                           convention=convention, period=period)

if __name__ == "__main__":
	app.run()