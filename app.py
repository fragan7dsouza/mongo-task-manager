import os
from datetime import datetime

from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
db_name = os.getenv("MONGO_DB_NAME", "mongo-task-manager")
collection_name = os.getenv("MONGO_COLLECTION", "tasks")

client = MongoClient(mongo_uri)
db = client[db_name]
tasks_collection = db[collection_name]


@app.get("/")
def index():
    tasks = list(tasks_collection.find().sort("created_at", -1))
    return render_template("index.html", tasks=tasks)


@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()

    if title:
        tasks_collection.insert_one(
            {
                "title": title,
                "subject": subject,
                "completed": False,
                "created_at": datetime.utcnow(),
            }
        )

    return redirect(url_for("index"))


@app.post("/toggle/<task_id>")
def toggle_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        tasks_collection.update_one(
            {"_id": ObjectId(task_id)}, {"$set": {"completed": not task.get("completed", False)}}
        )

    return redirect(url_for("index"))


@app.post("/delete/<task_id>")
def delete_task(task_id):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)