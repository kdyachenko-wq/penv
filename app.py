from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Вітання! Це мій перший сервер на Flask!</h1>"

@app.route("/about")
def about():
    return "<p>Цей вебсайт створено студентом 1-го курсу на занятті з фреймворків.</p>"

@app.route("/user/<name>")
def greet_user(name):
    return f"<h2>Привіт, {name}! Ласкаво просимо на наш сервер.</h2>"

if __name__ == "__main__":
    app.run(debug=True)  # Тепер усі маршрути зареєстровані до запуску