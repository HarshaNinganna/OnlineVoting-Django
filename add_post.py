from flask import Flask, request, redirect, url_for, session
from your_database_module import db, Post  # Adjust imports according to your database setup

app = Flask(__name__)

# Assuming you have your database model for posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_type = db.Column(db.String(20), nullable=False)

@app.route('/add_post', methods=['POST'])
def add_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    post_content = request.form.get('post_content')
    post_type = request.form.get('post_type')
    user_id = session['user_id']

    if post_content:
        # Create a new post
        new_post = Post(user_id=user_id, content=post_content, post_type=post_type)
        
        # Add and commit to the database
        db.session.add(new_post)
        db.session.commit()

    return redirect(url_for('home'))  # Redirect to home after adding the post

if __name__ == '__main__':
    app.run(debug=True)
