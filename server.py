from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'asecretkey'

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
  session['name']     = request.form['name']
  session['location'] = request.form['location']
  session['favlang']  = request.form['favlang']
  session['comment']  = request.form['comment']
  any_errors          = False

  if (len(session['name']) < 1):
    flash('Name field was not long enough.')
    any_errors = True

  if (len(session['comment']) < 1):
    flash('Comment field was not long enough.')
    any_errors = True

  if (len(session['comment']) > 120):
    flash('Comments must be less than 120 characters.')
    any_errors = True

  if not any_errors:
    return redirect('/result')
  else:
    return redirect('/')

@app.route('/result')
def result():
  # print form_info
  return render_template('result.html')


app.run(debug=True)
