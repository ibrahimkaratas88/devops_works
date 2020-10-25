# Import Flask modules
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

# Create an object named app
app = Flask(__name__)

# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = 'yeni phonebook'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qaz3228@wsx'
app.config['MYSQL_DATABASE_DB'] = 'phonebook'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Create users table within MySQL db and populate with sample data
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXISTS phonebook;'
users_table = """
CREATE TABLE phonebook (
  name varchar(50) NOT NULL,
  surname varchar(50),
  number integer,
  PRIMARY KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""  # Bu kullanım aslında sqlite ile aynı şeyi ifade etmekle birlikte bazı mysql convention'dan dolayı küçük farklılıklar ouşmaktadır. Bunlardan biri varchar olarak 50 dememiz gerekiyor burada. Ayrıca en sonda ENGINE tipi belirtmemiz gerekmektedir.
data = """
INSERT INTO phonebook.phonebook 
VALUES 
    ("ibrahim", "tektek", "54878954566"),
"""
cursor.execute(drop_table)
cursor.execute(users_table)
cursor.execute(data)
# cursor.close()
# connection.close()

# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.
def find_names(keyword):
    query = f"""
    SELECT * FROM phonebook WHERE username like '%{keyword}%';
    """
    cursor.execute(query)  
    result = cursor.fetchall()
    user_names = [(row[0], row[1]) for row in result]
    # if there is no user with given name in the db, then give warning
    if not any(user_names):
        user_names = [('Böyle bir kayıt bulunmamaktadır')]
    return user_names

# Write a function named `insert_email` which adds new email to users table the db.
def insert_name(name, surname, numbers):
    query = f"""
    SELECT * FROM phonebook WHERE username like '{name}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    # default text
    response = 'Error occurred..'
    # if user input are None (null) give warning
    if name == None or numbers == None:
        response = 'Username or number can not be emtpy!!'
    # if there is no same user name in the db, then insert the new one
    elif not any(result):
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{surname}','{numbers}');
        """
        cursor.execute(insert)
        response = f'User {name} {surname} added successfully'
    # if there is user with same name, then give warning
    else:
        response = f'User {name} {surname} already exits.'
    return response

# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')
@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_name = request.form['username']
        user_numbers = find_names(user_name)
        return render_template('numbers.html', name_numbers=user_numbers, keyword=user_name, show_result=True)
    else:
        return render_template('numbers.html', show_result=False)

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['useremail']
        result = insert_email(user_name, user_email)
        return render_template('add-email.html', result_html=result, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)