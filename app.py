from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nidhi92'
app.config['MYSQL_DB'] = 'portfolio'

def connect_to_database():
    mydb = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return mydb

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Function to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        gender = request.form['gender']
        Email = request.form['email']
        Password = request.form['password']
        Month = request.form['Month']
        Date = request.form['Date']
        Year = request.form['Year']

        # Connect to the database
        mydb = connect_to_database()
        mycursor = mydb.cursor()

        sql = """INSERT INTO register 
                 (FirstName, LastName, gender, Email, Password, Month, Date, Year) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (FirstName, LastName, gender, Email, Password, Month, Date, Year)
        
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.close()
        mydb.close()

        return redirect(url_for('login'))  # make sure you have a /login route

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
