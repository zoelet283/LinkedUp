from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'


cnx = mysql.connector.connect(user='root',
                              password='Nyamedia24#',
                              host='localhost',
                              database='sys')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
    
   
    cursor = cnx.cursor()

   
    query = 'SELECT * FROM users WHERE username = %s AND password = %s'
    cursor.execute(query, (username, password))

    
    results = cursor.fetchall()

    
    if results:
        session['username'] = username
        return redirect('/dashboard')

    
    else:
        return redirect('/Registration')

@app.route('/Registration',methods=['POST'])
def Registration():
    return render_template('Registration.html')
    

@app.route('/signup', methods=['POST'])
def signup():
    
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    cursor = cnx.cursor()
    query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
    cursor.execute(query, (username, password, email))
    cnx.commit()
    cursor.close()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/profile_card')
def profile_card():
    return render_template('profile_card.html')

@app.route('/profile_card2')
def profile_card2():
    return render_template('profile_card2.html')

@app.route('/profile_card3')
def profile_card3():
    return render_template('profile_card3.html')

if __name__ == '__main__':
    app.run(debug=True)


# Resources 
# https://freefrontend.com/css-login-forms/