from flask import render_template, request, redirect, url_for
from flask import Blueprint

routes_bp = Blueprint("routes", __name__)


def setup_routes(app):
    app.register_blueprint(routes_bp)


@routes_bp.route("/")
def home():
    return render_template("index.html")


@routes_bp.route("/add_task", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    print(f"New Task: {task_name}")  # Placeholder (will later save to DB)
    return redirect(url_for("routes.home"))
