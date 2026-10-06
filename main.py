from flask import Flask, request, session, redirect, url_for, render_template_string
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    if "username" in session:
        return f'Logged in as {session["username"]} | <a href="/logout">Logout</a>'
    return '<p>Hello, World!</p> | <a href="/login">Login</a>'


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template_string("""
        <form method="post">
            <p><input type="text" name="username" placeholder="Username">
            <p><input type="submit" value="Login">
        </form>
    """)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 - Page Not Found</h1>", 404
