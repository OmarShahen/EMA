from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('الصفحة-المقصودة.html')