# Online Voting System

## Project Overview
The **Online Voting System** is a secure, web-based application built using the Django framework. It is designed to enable voters to cast their ballots remotely via the internet, offering a secure, efficient, and accessible alternative to traditional paper-based voting. The system is user-friendly, with OTP-based authentication to verify user identities and ensure the integrity of each vote. 

This project also includes an admin interface to manage users, elections, and results. The front-end of the system is responsive, ensuring seamless operation on both desktops and mobile devices.

---

## Key Features
### 1. **User Authentication**
   - Users must register and authenticate their identity using OTP (One-Time Password) for secure login and voting.

### 2. **Secure Voting Process**
   - Each voter can cast their vote only once, and the votes are securely stored in the database.
   - All voting data is encrypted to ensure the security and integrity of the election process.

### 3. **Admin Dashboard**
   - Admins can manage the election, approve/reject users, view statistics, and manage the results of the election.

### 4. **Responsive Design**
   - The interface is built using **Bootstrap**, making it responsive and accessible across devices, including mobile phones and tablets.

### 5. **OTP Integration**
   - OTP verification is used for a secure voting process and login, ensuring only verified users can cast votes.

### 6. **Election Management**
   - Admins can create, edit, and delete elections, candidates, and view voting results.

---

## Technologies Used

### Backend:
- **Django Framework (Python)**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Django Authentication**: Used for handling user registration and login.
- **Requests Library**: For making HTTP requests in Python.

### Frontend:
- **HTML5**: Markup language for structuring web content.
- **CSS3**: Stylesheet language for designing the user interface.
- **Bootstrap**: CSS framework for responsive design.
- **JavaScript**: For interactive components and form validation.

### Database:
- **SQLite**: Lightweight, file-based database used to store user data, votes, and election details.

### Development Tools:
- **Virtual Environment**: For managing project-specific dependencies.
- **Git**: Version control for tracking code changes and collaboration.

---

## Installation Instructions

### 1. Prerequisites
Before installing and running the project, ensure you have the following:
- **Python 3.x** installed.
- **Django** installed.
- **SQLite** (which comes with Python).

### 2. Setup and Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/HarshaNinganna/OnlineVoting-Django.git
cd OnlineVoting-Django
