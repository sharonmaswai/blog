from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()],render_kw={"placeholder": "Title"})
    blog_data = TextAreaField('Type Blog here', validators=[Required()])
    photo_url = StringField('Photo URL', validators=[Required()], render_kw={'placeholder': 'Photo URL'})
    post = SubmitField('Post Blog')
