from flask import render_template,  request, redirect, url_for, flash, abort
from . import main
from ..models import User, Blog, Comment
from datetime import datetime
from .forms import BlogForm, CommentForm, EmailForm
from flask_login import login_required


from .. import db
 
@main.route('/')
def index():
    name='The Country Bowl'

    # random_quote = display_random_quote()

    all_blogs = Blog.get_all_blogs()

    
    blogs = all_blogs
    
    form = EmailForm()

    # if form.validate_on_submit():
    #     user_name = form.name.data
    #     user_email = form.email.data

    #     new_subscription = Email(name=user_name,email_data=user_email)
    #     new_subscription.save_email()

    #     send_subscriptions(new_subscription)
    #     return redirect(url_for('main.subscribe'))  
        
    return render_template('index.html', all_blogs=blogs, name=name, subscribe_form = form )
      
       

   

@main.route('/new_blog', methods=['GET', 'POST'])
@login_required

def new_blog():
    blogform=BlogForm()

    if blogform.validate_on_submit():

        blog_title=blogform.title.data
        blog=blogform.blog_data.data
        url=blogform.photo_url.data

        new_blog=Blog(title=blog_title, blog_content = blog, date_posted=datetime.now(),photo_url=url)
        new_blog.save_blog()

        new_blog.save_blog()
        return redirect(url_for('main.view_blog',id=new_blog.id))

    return render_template('new_blog.html', blogform = blogform)


@main.route('/blog/<int:id>', methods=['GET','POST'])
def view_blog(id):
    get_blog=Blog.query.get(id)

    # if get_blog is None:
        # abort(404)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        user_name = comment_form.name.data
        user_email = comment_form.email.data
        user_comment = comment_form.comment_data.data

        new_comment = Comment(name=user_name,email=user_email,comment_content=user_comment,date_comment = datetime.now(),blog_id=id)
        new_comment.save_comment()

        return redirect(url_for('main.view_blog',id=id))
    
    get_comments = Comment.get_blog_comments(id)

    


    return render_template('blog.html', get_blog=get_blog,get_comments=get_comments,comment_form=comment_form)

@main.route('/index/<int:id>/delete_blog')
@login_required
def delete_blog(id):
    blog = Blog.get_single_blog(id)

    db.session.delete(blog)
    db.session.commit()

    flash('Blog has been deleted') 

    return redirect(url_for('main.index'))

@main.route('/subscribe')
def subscribe():
    
    name='Successfully subscribed!!'

    return render_template('subscribed.html', name=name)
@main.route('/blog/<int:id>/<int:id_comment>/delete_comment')
@login_required
def delete_comment(id,id_comment):
    comment = Comment.get_single_comment(id,id_comment)

    db.session.delete(comment)
    db.session.commit()

   

    return redirect(url_for('main.view_blog',id=id))

