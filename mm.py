from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/data', methods=['post'])
def data():
    firstname = request.form.get('First_Name')
    Phonenumber = request.form.get('Phone_number')
    Email = request.form.get('email')
   

    print(firstname , Phonenumber, Email)
    return 'data received'
    return 'data received'

app.run(debug = True) # should be always at 