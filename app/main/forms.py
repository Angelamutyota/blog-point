from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class UploadBlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators=[Required()])
    blog =  TextAreaField('your blog',validators=[Required()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Type comment:',validators=[Required()])
    submit = SubmitField('Comment')
