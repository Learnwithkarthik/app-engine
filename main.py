from flask import Flask, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>App Engine Login Demo</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f6f8;
                text-align: center;
                padding-top: 80px;
            }
            .box {
                background: white;
                padding: 30px;
                width: 350px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #ccc;
            }
            input {
                width: 90%;
                padding: 10px;
                margin: 10px;
            }
            button {
                padding: 10px 25px;
                background: #1a73e8;
                color: white;
                border: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Login Application</h2>
            <form action="/login" method="post">
                <input type="text" name="username" placeholder="Enter username" required><br>
                <input type="password" name="password" placeholder="Enter password" required><br>
                <button type="submit">Login</button>
            </form>
            <p>Username: admin</p>
            <p>Password: admin123</p>
        </div>
    </body>
    </html>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))
    else:
        return """
        <h2>Login Failed</h2>
        <p>Invalid username or password.</p>
        <a href="/">Try Again</a>
        """

@app.route("/dashboard")
def dashboard():
    return """
    <html>
    <head>
        <title>Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background-color: #e8f0fe;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: white;
                padding: 30px;
                width: 400px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #ccc;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to Dashboard</h1>
            <p>Your application is running on Google App Engine.</p>
            <a href="/">Logout</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
