 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    email_address = first_name + '.' + last_name + '@gmail.com'

    return render_template('output.html', email_address=email_address)

if __name__ == '__main__':
    app.run()


main.py


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    email_address = first_name + '.' + last_name + '@gmail.com'

    return render_template('output.html', email_address=email_address)

if __name__ == '__main__':
    app.run()
