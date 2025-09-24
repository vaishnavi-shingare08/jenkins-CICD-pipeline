from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Simple form submission
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template("greet.html", name=name)

if __name__ == '__main__':
    # Flask now listens on container port 5000
    app.run(host='0.0.0.0', port=5000)
