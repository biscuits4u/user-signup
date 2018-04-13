from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup')
def display_use_signup_form():
    return render_template('index.html')

# VALIDATION FUNCTIONS

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

#CREATES ROUTE TO PROCESS AND VALIDATE THE FORM

@app.route("/signup", methods=['POST'])
def user_signup_complete():


    # CREATES VARIABLES FROM FORM INPUTS

    username = request.form['username']
    password = request.form['password']
    password_validate = request.form['password_validate']
    email = request.form['email']

    # CREATES EMPTY STRINGS FOR ERROR MESSAGES

    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    # ERROR MESSAGES

    error_required_field = "Required field"
    error_reenter_password = "Please reenter your password"
    error_char_count = "must be between 3 and 20 characters"
    error_no_spaces = "cannot contain spaces"

    # PASSWORD VALIDATION

    if not empty_val(password):
        password_error = error_required_field
        password = ''
        password_validate = ''
    elif not char_length(password):
        password_error = "Password " + error_char_count
        password = ''
        password_validate = ''
        password_validate_error = error_reenter_password
    else:
        if " " in password:
            password_error = "Password " + error_no_spaces
            password = ''
            password_validate = ''
            password_validate_error = error_reenter_password

    # SECOND PASSWORD VALIDATION

    if password_validate != password:
        password_validate_error = "Passwords must match"
        password = ''
        password_validate = ''
        password_error = 'Passwords must match'

    # USERNAME VALIDATION

    if not empty_val(username):
        username_error = error_required_field
        password = ''
        password_validate = ''
        password_error = error_reenter_password
        password_validate_error = error_reenter_password
    elif not char_length(username):
        username_error = "Username " + error_char_count
        password = ''
        password_validate = ''
        password_error = error_reenter_password
        password_validate_error = error_reenter_password
    else:
        if " " in username:
            username_error = "Username " + error_no_spaces
            password = ''
            password_validate = ''
            password_error = error_reenter_password
            password_validate_error - error_reenter_password

    # EMAIL VALIDATION

    if empty_val(email):
        if not char_length(email):
            email_error = "Email " + error_char_count
            password = ''
            password_validate = ''
            password_error = error_reenter_password
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            password_validate = ''
            password_error = error_reenter_password
            password_validate_error = error_reenter_password
        elif not email_at_symbol_more_than_one(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            password_validate = ''
            password_error = error_reenter_password
            password_validate_error = error_reenter_password
        elif not email_period(email):
            email_error = "Email must contain ."
            password = ''
            password_validate = ''
            password_error = error_reenter_password
            password_validate_error = error_reenter_password
        elif not email_period_more_than_one(email):
            email_error = "Email must contain onlye one ."
            password = ''
            password_validate = ''
            password_error = error_reenter_password
            password_validate_error = error_reenter_password
        else:
            if " " in email:
                email_error = "Email " + error_no_spaces
                password = ''
                password_validate = ''
                password_error = error_reenter_password
                password_validate_error = error_reenter_password

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)
        
@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()