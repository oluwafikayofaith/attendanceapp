#import os, random,string
from flask import render_template,request,session,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from attendanceapp import app,db
from attendanceapp.models import Students,Level
from attendanceapp.forms import MyForm
from attendanceapp import csrf



#route to the homepage
@app.route('/index')
def index():
    return render_template('student/homepage.html')        

#route to logout
@app.route('/studentlogout')
def student_logout():
    if session.get('student')!=None:
        session.pop('student',None)
    return redirect('/index')

#route to register a student
@app.route('/studentsignup',methods=['POST','GET'])
def student_signup():
    #instantiate an object of MyForm
    myform = MyForm()
    if request.method =='GET':
        level = Level.query.all()
        return render_template('student/studreg.html',myform=myform,level=level)
    else:
        if myform.validate_on_submit():
            fullname=request.form.get('fullname')
            email=request.form.get('email')
            password=request.form.get('password')
            confirm_password=request.form.get('confirm_password')
            matno=request.form.get('matno')
            add=request.form.get('add')
            phone=request.form.get('phone')
            levelid=request.form.get('levelid')
            hashed_pwd=generate_password_hash(password)
            hashed_cpwd=generate_password_hash(confirm_password)
            stud=Students(student_fullname=fullname,student_levelid=levelid,student_email=email,student_pwd=hashed_pwd,student_cpwd=hashed_cpwd,student_matno=matno,student_add=add,student_phone=phone)
            db.session.add(stud)
            db.session.commit()
            id=stud.student_id
            session['student']=id
            flash('Registration successful')
            return redirect(url_for('student_profile'))
        else:
            return render_template('student/studreg.html',myform=myform)
        
            
@app.route('/studlogin',methods=['POST','GET'])
def student_login():
    myform = MyForm()
    if request.method == 'GET':
        return render_template('student/studlogin.html',myform=myform)
    else:
        matno=request.form.get('matno')
        password=request.form.get('password')
        studdeets=db.session.query(Students).filter(Students.student_matno==matno).first()
        if studdeets !=None:
            pwd_indb=studdeets.student_pwd
            check=check_password_hash(pwd_indb,password)
            if check:
                session['student']=studdeets.student_id
                return redirect(url_for("student_profile"))
            else:
                flash('invalid password')
                return render_template('student/studlogin.html',myform=myform)
        else:
            flash('invalid password')
            return render_template('student/studlogin.html')

@app.route('/studprofile')
def student_profile():
    if session.get('student') != None:
        #retrieve the details of the logged in lecturer
        id=session['student']
        level = Level.query.first()
        studdeets=db.session.query(Students).get(id)
        return render_template('student/student_dash.html',studdeets=studdeets,level=level)
    else:
        return redirect(url_for('student_login'))
    

#route to edit profile
@app.route('/profile',methods=["POST","GET"])
@csrf.exempt
def profile():
    id=session.get('student')
    if id == None:
        return redirect(url_for('student_login'))
    else:
        if request.method == 'GET':
            studdeets=db.session.query(Students).get(id)
            return render_template ('student/student_profile.html',studdeets=studdeets)
        else:
            fullname=request.form.get('fullname')
            email=request.form.get('email')
            add=request.form.get('matno')
            phone=request.form.get('phone')
            #update db 
            studdeets=db.session.query(Students).get(id)
            obj=db.session.query(Students).get(id)
            obj.student_fullname=fullname
            obj.student_phone=phone
            obj.student_email=email
            obj.student_add=add
            db.session.commit()
            flash('profile updated')
            return render_template("student/student_dash.html",studdeets=studdeets)



