from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="itsneha",
    password="nehasql@134",
    db="db1")

mydb_write = mysql.connector.connect(
    host="localhost",
    user="itsneha",
    password="nehasql@134",
    db="db1")

cursor = mydb.cursor()
write_cursor = mydb_write.cursor()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM login WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user and user[3] == password:
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('homepage.html')

if __name__ == '_main_':
    app.run(debug=True)
