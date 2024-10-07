from flask import Flask
from models import db
from controllers import doctor_clinic_bp, user_bp, super_admin_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitalq.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register Blueprints
app.register_blueprint(doctor_clinic_bp)
app.register_blueprint(user_bp)
app.register_blueprint(super_admin_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
