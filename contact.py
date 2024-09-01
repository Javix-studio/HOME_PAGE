from flask import Flask, request, render_template
import yagmail # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact.html')  # This should be your HTML file.

@app.route('/send-email', methods=['POST'])
def send_email():
    to = request.form['to']
    subject = request.form['subject']
    message = request.form['message']

    # Replace with your email and password
    yag = yagmail.SMTP("rajadurai14008@gmail.com", "RAJA1.1.")

    # Sending the email
    yag.send(to=to, subject=subject, contents=message)

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)

