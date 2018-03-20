from flask import Flask, render_template, flash, request, session
from wtforms import Form, validators, StringField, RadioField
from qrgen import qrgenutils


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])

@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        content = request.form['name']
        print content
        img_filename = qrgenutils.generate_and_save_png(content)
        print img_filename
        html_table = '<img src="/static/generated_qr/' + img_filename + '"' + 'alt="QR Code should be here fuck !!!">'
        if form.validate():
            flash(html_table)
        else:
            flash('All the form fields are required. ')
    return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)