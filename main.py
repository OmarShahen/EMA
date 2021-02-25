from flask import Flask, render_template, request, url_for, jsonify, redirect

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('الصفحة-المقصودة.html')


@app.route('/forms-submission', methods=["POST"])
def forms():
    user_name = request.form.get('user_name')
    user_email = request.form.get('user_email')
    user_phone = request.form.get('user_phone')
    user_message = request.form.get('user_message').strip()
    return redirect(url_for('landing_page'))






if __name__ == "__main__":
    app.run(debug=True)