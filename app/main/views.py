from flask import render_template,  request, redirect, url_for, flash, abort
from . import main
from ..models import User, Blog, Comment
from datetime import datetime
from .forms import BlogForm, CommentForm, EmailForm

 
@main.route('/')
def index():
    name='The Rustic Life'


    return render_template('index.html', name=name)

@main.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    blogform=BlogForm()

    if blogform.validate_on_submit():

        blog_title=blogform.title.data
        blog=blogform.blog_data.data
        url=blogform.photo-url.data

        new_blog=Blog(title=blog-title, blog_content=blog, date_posted=datetime.now(),photo_url=url)
        new_blog.save_blog()

        send_blogs(new_blog)
        return redirect(url_for('main.blog',id=new_blog.id))

@main.route('/blog/<int:id>', methods=['GET','POST'])
def blog(id):
    post_blog=Blog.query.get(id)

    if get_blog is None:
        abort(404)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        user_name = comment_form.name.data
        user_email = comment_form.email.data
        user_comment = comment_form.comment_data.data

        new_comment = Comment(name=user_name,email=user_email,comment_content=user_comment,date_comment = datetime.now(),blog_id=id)
        new_comment.save_comment()

        return redirect(url_for('main.blog',id=id))
    
    get_comments = Comment.get_blog_comments(id)

    return render_template('blog.html', blog_format=blog_format, get_blog=get_blog, title="Blog", comment_form=comment_form, get_comments=get_comments, comments_count = len(get_blog_comments))

