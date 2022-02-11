from flask import Flask,flash, redirect, render_template, request, url_for,session
import psycopg2
try:
    conn=psycopg2.connect("dbname='huddle' user='postgres' host='localhost' password='vicciSQL'")
    print("Successful D.B Connection")
except:
    print("Connection error!")

app =Flask(__name__)
app.secret_key="123secrete kye"

@app.route('/')
def ims():
    return render_template("huddleims.html")

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
        return render_template("huddlereg.html")

@app.route('/log_in',methods=["post"])
def log_in():
    cur=conn.cursor()
    user_name=request.form('user_name')
    password=request.form("password")
    if user_name==user_name:
        print("hbbvhjv")
    else:
       print("pasdjskjfvf")
    data=(user_name,password)
    cur.execute(data)
    conn.commit()
    # return redirect(url_for('chat')) 

@app.route('/chatroom')
def chat():
    return render_template("huddlechat.html")

@app.route('/comments')
def coments():
    return render_template("chatrrom.html")
app.run(debug=True)