from flask import Flask, render_template, request 
from forms import MyFrom
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, you are in home page!!</h1>'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = MyFrom(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # validation of email   
        try:
            validate_email(email)
        except EmailNotValidError as e:
            return str(e)


        return render_template('success.html', name=name, email=email, message=message)

    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)