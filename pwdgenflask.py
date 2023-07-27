import random
import re
from flask import Flask, request, render_template
import twilio
from twilio.rest import Client

account_sid = 'ACfc5fa130a484b417e270870b16eece61'
auth_token = '07fda4421c60f166562fd925bc9d0a87'
twilio_phone_number = '+15392142533'

app = Flask(__name__, template_folder='templates')
client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['nameInput']
        phone_number = request.form['phoneInput']
        global para_input
        para_input = name
        final_otp = generate_password()
        send_sms(final_otp, phone_number)
    return render_template('index.html')
    return """
    <form method="post">
        <label for="nameInput">Enter your name:</label>
        <input type="text" id="nameInput" name="nameInput" required>
        <input type="submit" value="Submit">
    </form>
    """

def generate_password():
    special_char = ['@', '#', '$', '%', '&']
    password = []
    capitalize_char1 = []
    pwd = ''
    upper_char = ''

    i = 0
    j = 0
    l = 0

    while i < 5:
        z = re.findall("[a-zA-Z]", para_input)  # Use regular expression to find alphabetic characters
        if z:
            password.append(random.choice(z))
            i += 1

    while j < 3:
        x = re.findall("\d", para_input)
        if x:
            password.append(random.choice(x))
            j += 1

    while l < 2:
        password.append(random.choice(special_char))
        l += 1

    capitalize_char = capitalize_char1.append(random.choice(list(filter(None, z))))
    uppercase = upper_char.join(capitalize_char1).upper()

    otp = pwd.join(password).replace(" ", "") + uppercase
    convert_toList = list(otp)
    random.shuffle(convert_toList)
    final_otp = ''.join(convert_toList).replace(" ", "")
    return final_otp
    

def send_sms(password, phone_number):
    try:
        message = client.messages.create(
            body=f"Your Generated Password: {password}",
            from_=twilio_phone_number,
            to=phone_number
        )
        print("SMS Sent Successfully!")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True)