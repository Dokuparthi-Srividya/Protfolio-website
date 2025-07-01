import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, render_template, request, send_file,redirect,url_for

app = Flask(__name__)
db=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor = db.cursor()
        sql = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)

        try:
            cursor.execute(sql, values)
            db.commit()
            return render_template('contact.html', success=True)
        except Exception as e:
            print("❌ Error:", e)
            db.rollback()
            return render_template('contact.html', success=False)
        finally:
            cursor.close()

    return render_template('contact.html')

@app.route('/resume')
def download_resume():
    return send_file('resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
