from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pulseconnect.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to save uploaded files

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database models
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    post_type = db.Column(db.String(20), nullable=False)
    media_file = db.Column(db.String(255), nullable=True)  # Add media_file field

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        friends = Friend.query.filter_by(user_id=user_id).all()
        posts = Post.query.order_by(Post.post_id.desc()).all()
        return render_template('home.html', friends=friends, posts=posts)
    return render_template('home.html', friends=[], posts=[])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.user_id
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/add_post', methods=['POST'])
def add_post():
    if 'user_id' in session:
        user_id = session['user_id']
        content = request.form['post_content']
        post_type = request.form['post_type']
        
        # Handle file upload
        media_file = request.files.get('file')
        media_filename = None

        if media_file:
            media_filename = media_file.filename
            media_file.save(os.path.join(app.config['UPLOAD_FOLDER'], media_filename))  # Save the file

        new_post = Post(user_id=user_id, content=content, post_type=post_type, media_file=media_filename)
        db.session.add(new_post)
        db.session.commit()

    return redirect(url_for('home'))

@app.route('/like_post/<int:post_id>', methods=['POST'])
def like_post(post_id):
    if 'user_id' in session:
        # Logic for liking a post
        # You can create a Likes model if you want to store likes in the database
        # For simplicity, this just redirects to home
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    if 'user_id' in session:
        user_id = session['user_id']
        content = request.form['comment_content']
        new_comment = Comment(user_id=user_id, post_id=post_id, content=content)
        db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/vote', methods=['POST'])
def vote():
    if 'user_id' in session:
        post_id = request.form['post_id']  # Retrieve the post ID from the form
        vote_value = request.form['vote']  # Retrieve the vote value (yes/no)

        # Handle the voting logic here
        # For example, you might want to save the vote to a database or update the post's state

        return redirect(url_for('home'))  # Redirect back to the home page
    return redirect(url_for('login'))  # Redirect to login if not authenticated

if __name__ == '__main__':
    app.run(debug=True)
