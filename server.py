from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# populate data from form request in here
form_info = {}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/survey', methods=['POST'])
def new_survey():
  # print "hello there"
  form_info['name'] = request.form['name']
  form_info['location'] = request.form['location']
  form_info['favlang'] = request.form['favlang']
  form_info['comment'] = request.form['comment']
  return redirect('/result')

@app.route('/result')
def result():
  print form_info
  return render_template('result.html', data=form_info)


app.run(debug=True)
