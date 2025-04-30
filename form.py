from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
  <body>
    <h2>Enter your name and email address:</h2>
    <form method="POST" action="/submit">
      Name: <input type="text" name="name"><br><br>
      Email Address: <input type="email" name="email"><br><br>
      <input type="submit" value="Submit">
    </form>
    <p>See all emails at <a href="/emails">/emails</a></p>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(form_html)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    with open('emaillist.txt', 'a') as f:
        f.write(f'Name: {name}\n')
        f.write(f'Email: {email}\n')
    return render_template_string('''
        <html>
        <head>
            <script type="text/javascript">
                alert("You are being redirected to the emails page.");
                window.location.href = "/emails";  // Redirect after alert
            </script>
        </head>
        <body>
        </body>
        </html>
    ''')
@app.route("/emails", methods=["GET"])
def emails():
    with open('emaillist.txt', 'r') as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(debug=True)
