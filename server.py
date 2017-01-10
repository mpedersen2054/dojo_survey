from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/survey', methods=['POST'])
def new_survey():
  print "hello there"
  # name, location, fav_lang, comment = request.form

@app.route('/result')
def result():
  return render_template('result.html')


app.run(debug=True)
