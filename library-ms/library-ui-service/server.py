from flask import Flask, render_template

app = Flask(__name__)

@app.route('/library')
def homepage():
    return render_template('index.html')  # render a template

app.run(port=8080, debug=True)
