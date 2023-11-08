 Design:

HTML files:
- index.html: This will be the main page of the application. It will have a form for the user to input their first and last name.
- output.html: This page will display the generated email address.

Routes:
- /: This route will render the index.html page.
- /generate: This route will take the first and last name from the form on the index.html page and generate the email address. It will then render the output.html page with the generated email address.

Flask Application:

```python
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
```