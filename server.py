from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'asecretkey'

# populate data from form request in here
form_info = {}

@app.route('/')
def index():
  if not 'name' in session:
    session['name'] = ''
  if not 'location' in session:
    session['location'] = ''
  if not 'favlang' in session:
    session['favlang'] = ''
  if not 'comment' in session:
    session['comment'] = ''
  return render_template('index.html')

@app.route('/survey', methods=['POST'])
def new_survey():
  # print "hello there"
  session['name']     = request.form['name']
  session['location'] = request.form['location']
  session['favlang']  = request.form['favlang']
  session['comment']  = request.form['comment']
  return redirect('/result')

@app.route('/result')
def result():
  # print form_info
  return render_template('result.html', data=form_info)


app.run(debug=True)
