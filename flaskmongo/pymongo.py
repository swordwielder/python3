from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)


@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.users.find_one_or_404({"_id": username})
    return render_template("user.html",
        user=user)


@app.route("/uploads/<path:filename>")
def get_upload(filename):
    return mongo.send_file(filename)


@app.route("/uploads/<path:filename>", methods=["POST"])
def save_upload(filename):
    mongo.save_file(filename, request.files["file"])
    return redirect(url_for("get_upload", filename=filename))


@app.route("/<ObjectId:task_id>")
def show_task(task_id):
    task = mongo.db.tasks.find_one_or_404(task_id)
    return render_template("task.html", task=task)


app = Flask(__name__)

# connect to MongoDB with the defaults
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/databaseOne")

# connect to another MongoDB database on the same host
mongo2 = PyMongo(app, uri="mongodb://localhost:27017/databaseTwo")

# connect to another MongoDB server altogether
mongo3 = PyMongo(app, uri="mongodb://another.host:27017/databaseThree")