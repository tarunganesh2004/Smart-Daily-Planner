from flask import render_template, request, redirect, url_for
from flask import Blueprint
from app.models import db, Task

routes_bp = Blueprint("routes", __name__)


def setup_routes(app):
    app.register_blueprint(routes_bp)


@routes_bp.route("/")
def home():
    tasks = Task.query.all()  # Fetch all tasks from the database
    return render_template("index.html", tasks=tasks)


@routes_bp.route("/add_task", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    if task_name:
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("routes.home"))
