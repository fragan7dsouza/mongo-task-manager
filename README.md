# Student Mongo Task Manager

Simple beginner project to learn MongoDB with Flask.

## Project structure

```text
mongo-task-manager/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
```

## What this app does

- Add student tasks (title + optional subject)
- Store tasks in MongoDB
- Mark tasks done/pending
- Delete tasks

## Requirements

- Python 3.10+
- MongoDB installed and running locally

## Setup

1. Create and activate a virtual environment:

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

2. Install dependencies:

	```powershell
	pip install -r requirements.txt
	```

3. Ensure MongoDB is running on your machine (default URI):

	```text
	mongodb://localhost:27017
	```

4. Check `.env` values (already included):

	```env
	MONGO_URI=mongodb://localhost:27017
	MONGO_DB_NAME=student_task_manager
	MONGO_COLLECTION=tasks
	```

## Run

```powershell
python app.py
```

Open http://127.0.0.1:5000

## MongoDB learning points in this project

- Create DB/collection automatically on first insert
- Insert docs with `insert_one`
- Query docs with `find` + `sort`
- Update docs with `update_one` and `$set`
- Delete docs with `delete_one`