# Online Voting System

## Project Overview
The **Online Voting System** is a secure, web-based application built using the Django framework. It enables voters to cast their ballots remotely via the internet, offering a secure, efficient, and accessible alternative to traditional paper-based voting. The system features user-friendly OTP-based authentication to verify user identities, ensuring the integrity of each vote.

The project includes an admin interface for managing users, elections, and results. The front-end is responsive, ensuring seamless operation across both desktop and mobile devices.

---

## Key Features
### 1. **User Authentication**
   - Users must register and authenticate their identity using OTP (One-Time Password) for secure login and voting.

### 2. **Secure Voting Process**
   - Each voter can cast their vote only once, and votes are securely stored in the database.
   - Voting data is encrypted to ensure security and integrity throughout the election process.

### 3. **Admin Dashboard**
   - Admins can manage elections, approve/reject users, view statistics, and manage election results.

### 4. **Responsive Design**
   - Built using **Bootstrap** for a responsive interface, ensuring accessibility on mobile and desktop devices.

### 5. **OTP Integration**
   - OTP verification is used for login and voting, ensuring only verified users can participate.

### 6. **Election Management**
   - Admins can create, edit, and delete elections, manage candidates, and view voting results.

---

## Technologies Used

### Backend:
- **Django Framework (Python)**: High-level web framework for rapid development.
- **Django Authentication**: Handles user registration and login.
- **Requests Library**: Used for making HTTP requests in Python.

### Frontend:
- **HTML5**: Markup language for structuring web content.
- **CSS3**: Stylesheet for designing the UI.
- **Bootstrap**: CSS framework for responsive design.
- **JavaScript**: Provides interactive components and form validation.

### Database:
- **SQLite**: Lightweight, file-based database used to store user data, votes, and election details.

### Development Tools:
- **Virtual Environment**: Used for managing project-specific dependencies.
- **Git**: Version control system for tracking code changes.

---

## Installation Instructions

### 1. Prerequisites
- **Python 3.x**
- **Django**
- **SQLite** (comes with Python)

### 2. Setup and Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/HarshaNinganna/OnlineVoting-Django.git
cd OnlineVoting-Django
```
Step 2: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
Step 4: Configure Database
```bash
python manage.py migrate
```
Step 5: Create a Superuser
```bash
python manage.py createsuperuser
```
Step 6: Run the Development Server
```bash
python manage.py runserver
```
3. Access the Platform
Client-side: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/

OnlineVoting-Django/
├── online_voting/        # Core project files
├── users/                # User registration, login, profile
├── elections/            # Election and voting logic
├── static/               # Static assets (CSS, JavaScript, images)
├── templates/            # HTML templates for frontend
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database file
├── requirements.txt      # Python dependencies
└── README.md             # Readme file

Features Breakdown
1. Security
User Authentication: Users must log in and verify their identity via OTP before voting.
Admin Authentication: Admins have secure login credentials to manage elections and results.
2. Election Management
Create Elections: Admins can set up elections with start/end dates and add candidates.
Vote Casting: Users can cast a single vote per election, and all votes are securely encrypted.
Results Display: Results are only displayed after the election ends to maintain fairness.
3. User Experience
Responsive Design: The platform is optimized for mobile, tablet, and desktop screens.
Real-time Voting: Users receive confirmation when their vote is successfully cast.
Error Handling: Clear error messages for incorrect login attempts or other issues.
Future Enhancements
Multi-language Support: Implementing support for multiple languages to reach a wider audience.
Advanced Analytics: Providing detailed statistics and voter turnout reports for admins.
Mobile App: Developing a mobile app version for even greater accessibility.
Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. For major changes, please open an issue to discuss the proposed improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.


This version ensures clarity and completeness, while maintaining professionalism for your GitHub repository.
