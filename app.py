from flask import Flask, render_template, request, url_for, jsonify, redirect
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/')
@app.route('/الرئسية')
def landing_page():
    return render_template('الصفحة-المقصودة.html')

@app.route('/اعمالنا')
def our_services():
    return render_template('خدمتنا.html')

@app.route('/تواصل-معنا')
def contact_us():
    return render_template('تواصل-معنا.html')

@app.route('/forms-submission', methods=["POST"])
def forms():
    
    user_name = request.form.get('user_name')
    user_email = request.form.get('user_email')
    user_phone = request.form.get('user_phone')
    user_message = request.form.get('user_message').strip()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Mail From The Website"
    message["From"] = user_email
    message["To"] = "mabdelhamed151@gmail.com"

    text = f"""Name: {user_name}\nE-mail: {user_email}\nPhone: {user_phone}\nMessage: {user_message}"""

    html = f"""
                <html>
                    <body>
                        <p>
                            Name: <strong>{user_name}</strong>
                            E-mail: <strong>{user_email}</strong>
                            Phone: <strong>{user_phone}</strong>
                            Message: <strong>{user_message}</strong>
                        </p>
                    </body>
                </html>
            """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login("emawebsitemail908@gmail.com", "abdelhamed77")
            server.sendmail("mabdelhamed151@gmail.com", "mabdelhamed151@gmail.com", message.as_string())
    except Exception:
        return redirect(url_for('landing_page'))
    
    return redirect(url_for('landing_page'))

    

if __name__ == "__main__":
    app.run(debug=True)