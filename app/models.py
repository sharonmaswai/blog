

class Blog(db.Model):


    __tablename__='blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    blog_pic = db.Column(db.String(255))
    photo_url = db.Column(db.String(500))
    
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    photo = db.relationship('Photo', backref='blog',lazy='dynamic')

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