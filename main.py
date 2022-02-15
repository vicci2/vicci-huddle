from flask import Flask,flash, redirect, render_template, request, url_for,session
import psycopg2
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import InputRequired,DataRequired, EqualTo, Length
from flask_login import UserMixin, login_user, login_manager,login_required,logout_user, current_user
# from datetime import datetime

app =Flask(__name__)
app.secret_key="123secrete kye"
# app.permanent_session_lifetime=timedelta(minutes=10)
try:
    conn=psycopg2.connect("dbname='huddle' user='postgres' host='localhost' password='vicciSQL'")
    # conn=psycopg2.connect("dbname='d4augsl57bdont' user='epbnudknwnktpp' port='5432' host='ec2-34-199-15-136.compute-1.amazonaws.com' password='863b87226bd0eafa17748cc14d4bdcb0af464d40c35796f8bf38cce8dc378153'")
    print("Successful D.B Connection")
except:
    print("Connection error!")

class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired(),Length(min=4, max=80)] )
    username=PasswordField('password',validators=[InputRequired(),Length(min=4, max=80)] )

@app.route('/')
def ims():
    return render_template("index.html")

@app.route('/register',methods=["GET","POST"])
def reg():
    cur=conn.cursor()
    if request.method == "POST":
        user_name=request.form["user_name"]
        age=request.form["age"]
        password=request.form["password"]
        # cpassword=request.form["cpassword"]
        country=request.form["country"]
        city=request.form["city"]
        street=request.form["street"]
        phone_number=request.form["phone_number"]
        second_phone_number=request.form["second_phone_number"]
        email_address=request.form["email_address"]
        
        query="INSERT INTO public.login (user_name, age, password, country, city, street, phone_number, second_phone_number, email_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        row=(user_name,age,password,country,city,street,phone_number,second_phone_number,email_address)
        cur.execute(query,row)
        conn.commit()
        flash("Registration successful!")
        return redirect(url_for('ims'))
    else:        
        flash("Please enter user details.")
        return render_template("huddlereg.html")

@app.route('/log_in',methods=["post"])
def log_in():
    cur=conn.cursor()
    user_name=request.form["user_name"]
    password=request.form["password"]
    query=""
    cur.execute(query)
    if user_name==user_name:
        print("hbbvhjv")
    else:
       print("pasdjskjfvf")
    data=(user_name,password)
    
    conn.commit()
    return redirect(url_for('chat'))
    

@app.route('/chatroom')
def chat():
    return render_template("huddlechat.html")

@app.route('/comments')
def coments():
    return render_template("chatrrom.html")
if __name__ == '__main__':    
    app.run(debug=True)