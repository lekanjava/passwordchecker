from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Your existing code here...


from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Common weak passwords list
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "abc123", "letmein"]

def check_password_strength(password, return_numeric=False):
    """
    Checks the strength of a password.

    :param password: The password to check.
    :param return_numeric: If True, returns numeric strength values (1 = Weak, 2 = Moderate, 3 = Strong).
    :return: Either a numeric value or a descriptive string.
    """
    # Check length
    if len(password) < 8:
        return 1 if return_numeric else "Weak (Password must be at least 8 characters long)"

    # Check for uppercase, lowercase, numbers, and special characters
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check if password is in common passwords list
    if password in COMMON_PASSWORDS:
        return 1 if return_numeric else "Weak (Common password detected)"

    # Evaluate strength
    if has_upper and has_lower and has_digit and has_special:
        return 3 if return_numeric else "Strong"
    elif has_upper or (has_lower and has_digit):
        return 2 if return_numeric else "Moderate"
    else:
        return 1 if return_numeric else "Weak"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("password")
        strength = check_password_strength(password)
        return render_template("index.html", strength=strength, password=password)
    return render_template("index.html", strength=None)



if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)

