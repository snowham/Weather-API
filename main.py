from flask import Flask, render_template, request
import tempRequest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['POST'])
def temperature():
    if request.method == 'POST':
        temp = tempRequest.temp(request.form['zip_code'], request.form['country'])
    return render_template('temperature.html', currTemp=temp)

if __name__ == '__main__':
    app.run(debug=True)
