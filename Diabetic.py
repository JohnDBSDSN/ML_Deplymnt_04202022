#from crypt import methods
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Diab1.html')

@app.route('/data1', methods=['post'])
def data1():
    Pregnancy = request.form.get('preg')
    Glucose = request.form.get('plas')
    BP = request.form.get('pres')
    Skin_Thickness = request.form.get('skin')
    Insulin = request.form.get('test')
    BMI = request.form.get('mass')
    DiabetesPf  = request.form.get('pedi')
    Age  = request.form.get('age')
    Outcome  = request.form.get('class')

    data3 = Pregnancy

    print(Pregnancy)
    print(Glucose)
    print(BP)
    print(Skin_Thickness)
    print(Insulin)
    print(BMI)
    print(DiabetesPf)
    print(Age)
    print(Outcome)
    
    return render_template('Diab_Disp.html', data3=data3)
    return "Data1 received !!"
    
    
     


    
#@app.route('/data', methods=['post'])
#def data():
#    firstname = request.form.get('First_Name')
#    Phonenumber = request.form.get('Phone_number')
#    Email = request.form.get('email')
   

 #   print(firstname , Phonenumber, Email)
 #   return 'data received'
 #   return 'data received'

app.run(debug = True) # should be always at 