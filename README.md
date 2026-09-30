# AcaDex
AcaDex - A simple Python CLI application for managing student attendance, assignments, subjects, and tasks.

## Features

### 📚 Subjects

* Add subjects to your academic list.
* View all added subjects.

### 📊 Attendance

* Add or update attendance for each subject.
* View attendance percentage for individual subjects.
* Calculate overall attendance percentage.

### 📝 Assignments

* Add assignments with:

  * Assignment name
  * Subject
  * Due date
* View all assignments.
* Mark assignments as completed.
* Track pending and completed assignments.

### 📈 Dashboard

The dashboard provides a quick overview of:

* Total number of subjects
* Overall attendance percentage
* Pending assignments
* Completed assignments

## Technologies Used

* **Python 3**
* Command Line Interface (CLI)
* Python Lists
* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input

## Requirements

* Python 3.x
* No external Python libraries are required.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AcaDex.git
```

### 2. Open the project folder

```bash
cd AcaDex
```

### 3. Run the program

```bash
python main.py
```

> Replace `main.py` with the name of your Python file if it is different.

## How It Works

When the program starts, the main menu provides five options:

```text
1. Subjects
2. Attendance
3. Assignments
4. Dashboard
5. Exit
```

Users can navigate through these options by entering the corresponding number.

## Data Storage

AcaDex currently stores data **temporarily in memory** using Python lists and dictionaries.

This means that subjects, attendance records, and assignments will be lost when the program is closed.

## Future Improvements

Possible improvements for future versions include:

* 💾 Save data permanently using files or a database
* 📅 Automatic due-date tracking
* 🔔 Assignment reminders
* 📊 More detailed academic statistics
* 🎨 Improved user interface
* 🔐 User accounts and login system
* 📱 Graphical user interface (GUI)

## Project Purpose

This project was created as a beginner-level Python project to practice fundamental programming concepts such as functions, loops, lists, dictionaries, conditional statements, and user input.

