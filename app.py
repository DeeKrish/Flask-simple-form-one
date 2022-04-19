from flask import Flask,request,render_template,flash,redirect,url_for,session
from form import simpleform
app=Flask(__name__)
app.secret_key = 'private_key'
#home page
@app.route('/')
def defaultHome():
    return render_template('home.html')

#login page
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        userName=request.form['name']
        userPassword=request.form['Password']
        if userName=='Admin' and userPassword=='admin':
            return render_template('dashboard.html', name=userName)
        else: return render_template('home.html')
    else:
        userName=request.args.get('name')
        return render_template('login.html',name=userName)

#registration form
@app.route('/registrationform', methods=['POST','GET'])
def registrationform():
    s= simpleform()
    if request.method== 'POST':
        session['name']=request.form['name']
        if s.validate()=='False':
            flash('Please fill out this field')
            return render_template('register.html', form=s)
        else: return redirect(url_for('successform'))
    elif request.method== 'GET':
        return render_template('register.html',form=s)

@app.route('/successform')
def successform():
    name=session.get('name', None)
    return render_template('successform.html')



if __name__ == '__main__':
    app.run(debug=True)