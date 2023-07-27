# Temporary-password-generator
This is a temporary password generator built with python. I used the Twilio API to send the OTPs to the provided phone number. I used the front end as HTML, CSS and JS its just a simple website where the user enters their name and employee code and also their phone number. The logic of this program is done through python.
So basically what happens is when i enter my name and employee code it generates the otp based on the input, it removes any white spaces, it takes 5 non-numeric characters, 3 numbers and 2 special characters and appends them to a list, then the list is jumbled and completely random, all the characters from the employee name and number are not taken only a few. then this jumbled list to converted to a string as the final output and sent as an sms to the provided phone number using twilio.
Im still thinking of implementing better logic, better ui in the website and also thought of integrating it with mysql, but thats for the future :D be sure to checkout this code on your systems as well.
Technologies used:
Python ( for logic)
twilio (for sending otp to phone number)
flask api(for backend)
VS code
HTML, CSS, JS front end
random library(python) for randomising the otp
regex library (python) for filtering and segregating the input
