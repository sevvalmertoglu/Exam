# Flask Quiz Web Application

This project is a Flask-based web application that provides a simple quiz platform. Users can enter their name, answer questions, and view their scores. The application also keeps track of the user's highest score and displays it as a percentage. You can access the live version of the project at [sevvalmertoglu.pythonanywhere.com](https://sevvalmertoglu.pythonanywhere.com/).

## Features

- **User Registration:** Users can enter their name before starting the quiz. The application stores user information and their highest scores in a SQLite database.
- **Quiz Questions:** Dynamically displays questions retrieved from a database.
- **Score Tracking:** Calculates the user's score and compares it to their previous highest score, updating it if they achieve a new high score.
- **High Score Display:** Displays the user's highest score as a percentage in the top-right corner of the quiz page.

## Technologies Used

- **Python:** Core programming language for the application.
- **Flask:** Framework for building the web application.
- **SQLite:** Database for storing user data and quiz questions.
- **HTML & CSS:** Frontend design.
  
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sevvalmertoglu/Exam.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Exam
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the SQLite database:
   ```bash
   python question.py 
   ```
6. Run the application:
   ```bash
   flask run
   ```
7. Access the application at `http://127.0.0.1:5000/` in your browser.

## Usage

1. Enter your username.
2. Answer the quiz questions.
3. Submit your answers to view your score and see if it beats your highest score.
4. Your highest score will be displayed in the top-right corner of the quiz page.

## Live Demo

The application is live and accessible at:
[https://sevvalmertoglu.pythonanywhere.com/](https://sevvalmertoglu.pythonanywhere.com/)

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## Author

**Şevval Mertoğlu**

Connect with me on [LinkedIn](https://www.linkedin.com/in/sevvalmertoglu8/).

