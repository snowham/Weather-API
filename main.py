from flask import Flask, render_template, request, flash
import tempRequest

app = Flask(__name__)

app.secret_key = 'thisisasecretdonttellanyonepleasejustkidding'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['POST'])
def temperature():
    if request.method == 'POST':
        try:
            temp = tempRequest.temp(request.form['zip_code'], request.form['country'])
        except KeyError:
            flash('Either zip-code or country was not found.', 'error')
            return render_template('index.html')
    return render_template('temperature.html', currTemp=temp)

if __name__ == '__main__':
    app.run(debug=True)
