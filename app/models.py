from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Blog(db.Model):


    __tablename__='blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    blog_pic = db.Column(db.String(255))
    photo_url = db.Column(db.String(500))
    
    # comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    # photo = db.relationship('Photo', backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by('-id').all()
        return blogs

    @classmethod
    def get_single_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(48), unique = True, index=True)
    email = db.Column(db.String(48),unique=True, index = True)
    password_hash = db.Column(db.String(255)) 

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)  