from flask import render_template
from . import main
 
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

        new_blog=Blog(title=blog-title, blog-content=blog, date_posted=datetime.now(),photo_url=url)
        new_blog.save_blog()

        send_blogs(new_blog)
        return redirect(url_for('main.blog',id=new_blog.id))

@main.route('/blog/<int:id>', methods=['GET','POST'])
def blog(id):
    post_blog=Blog.query.get(id)

    if get_blog is None:
        abort(404)

    




