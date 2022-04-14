from flask import Flask,flash, redirect, render_template, request, url_for,session
import psycopg2
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
# from wtforms.validators import InputRequired,DataRequired, EqualTo, Length
# from flask_login import UserMixin, login_user, login_manager,login_required,logout_user, current_user


app =Flask(__name__)
app.secret_key="123secrete kye"
# app.permanent_session_lifetime=timedelta(minutes=10)
try:
    conn=psycopg2.connect("dbname='huddle' user='postgres' host='localhost' password='vicciSQL'")
    # conn=psycopg2.connect("dbname='dk28dn22dcnb2' user='lwbdaaftujgejr' port='5432' host='ec2-54-194-147-61.eu-west-1.compute.amazonaws.com' password='cda07fc755061b7a120e7fa2d8f6144dc6268aa98131ef59eeefe2fa3d32da00'")
    print("Successful D.B Connection")
except:
    print("Connection error!")


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register',methods=["GET","POST"])
def reg():
    
    cur=conn.cursor()
    if request.method == "POST":
        user_name=request.form["user_name"]
        age=request.form["age"]
        password=request.form["password"]             
        phone_number=request.form["phone_number"]
        second_phone_number=request.form["second_phone_number"]
        email_address=request.form["email_address"] 
        if len(password)>=5:
            query="INSERT INTO public.login (user_name, age, password,phone_number, second_phone_number, email_address) VALUES (%s,%s,%s,%s,%s,%s);"
            row=(user_name,age,password,phone_number,second_phone_number,email_address)
            cur.execute(query,row)
            conn.commit()
            flash("Registration successful!","success")
            return redirect(url_for('home'))
        else:        
            flash("Please enter user details.","danger")
            # flash("User password must have atleast 5 charecters and must not be the username")
            return redirect(url_for("sign_up"))
    else:
        return redirect(url_for("sign_up"))
        

@app.route('/sign_up')
def sign_up():
    return render_template("huddlereg.html")

@app.route('/log_in',methods=["GET","POST"])
def log_in():
    cur=conn.cursor()
    if request.method=='POST':
        user_name=request.form["user_name"]
        password=request.form["password"]
        query="SELECT user_name,password FROM public.login; "
        row=(user_name,password)
        cur.execute(query,row)
        abc=cur.fetchall()
        print("here is abc",abc)
        for i in abc:
            if user_name==i[0] and password==i[1]:
                print(i[0],i[1])
                user = i[0]
                flash("Login Successful!","success")
                return render_template('huddlechat.html',user=user)
            else:
                flash("Invalid User Details.Try Again!","Warning")
                return redirect(url_for('home'))
    else:     
        return render_template('index.html')        

@app.route('/chatroom')
def chat():
    return render_template("huddlechat.html")

@app.route('/coment',methods=["GET","POST"])
def coment():
    flash("Invalid user details", "warning")
    return render_template('index.html')

@app.route('/comments')
def comments():
    return render_template("chatrrom.html")

if __name__ == '__main__':    
    app.run(debug=True)