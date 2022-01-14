from flask import Flask, render_template, request
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

ckeditor = CKEditor(app)

class CommentForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    comment = CKEditorField("Commento", validators=[DataRequired()])
    submit = SubmitField('Invia')


@app.route('/', methods=["GET", "POST"])
def index():
    my_form = CommentForm()
    if my_form.validate_on_submit():
        my_name = request.form['name']
        my_comment = my_form.comment.data
        return render_template('comment.html', name=my_name, comment=my_comment)
    return render_template('index.html', form=my_form)

if __name__ == "__main__":
    app.run(debug=True)