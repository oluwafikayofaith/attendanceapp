import os,random,string
from flask import render_template,request,session,flash,redirect,url_for
#from sqlalchemy import or_
#from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash,check_password_hash
from attendanceapp import app,db
from attendanceapp.models import Lecturers,Students,Timetable,Attendance,Course
from attendanceapp.forms import LectureForm
from attendanceapp import csrf


def generate_name():
    filename = random.sample(string.ascii_lowercase,10)#this will return a list
    return ''.join(filename)

#creating routes

@app.route('/')
def home():
    return render_template('lecturer/homepage.html')

@app.route('/lecturerlogout')
def lecturer_logout():
    #pop the session and redirect to home page
    if session.get('lecturer')!=None:
        session.pop('lecturer',None)
    return redirect('/')


@app.route('/lectsignup',methods=['POST','GET'])
def lect_signup():
    lectureform=LectureForm()
    if request.method =='GET':
        return render_template('lecturer/lecturerreg.html',lectureform=lectureform)
    else:
        if lectureform.validate_on_submit():
            fullname=request.form.get('fullname')
            email=request.form.get('email')
            password=request.form.get('password')
            add=request.form.get('add')
            phone=request.form.get('phone')
            confirm_password=request.form.get('confirm_password')
            hashed_pwd=generate_password_hash(password)
            hashed_cpwd=generate_password_hash(confirm_password)
            lec=Lecturers(lecturer_fullname=fullname,lecturer_phone=phone,lecturer_add=add,lecturer_email=email,lecturer_pwd=hashed_pwd,lecturer_cpwd=hashed_cpwd)
            db.session.add(lec)
            db.session.commit()
            lectid=lec.lecturer_id
            session['lecturer']=lectid
            return redirect(url_for('lect_profile'))
        else:
            flash('You must complete all the fields to signup')
            return render_template('lecturer/lecturerreg.html',lectureform=lectureform)
            

@app.route('/lectlogin',methods=['POST','GET'])
def lect_login():
    lectureform=LectureForm()
    if request.method =='GET':
        return render_template('lecturer/lecturerlogin.html',lectureform=lectureform)
    else:
        #retrieve the form data
        email=request.form.get('email')
        password=request.form.get('password')
        lecdeets=db.session.query(Lecturers).filter(Lecturers.lecturer_email==email).first()
        if lecdeets != None:
            pwd_indb= lecdeets.lecturer_pwd
            chk=check_password_hash(pwd_indb,password)
            if chk:
                id= lecdeets.lecturer_id
                session['lecturer']=id
                return redirect (url_for("lect_profile"))
            else:
                flash("invalid password")
                return redirect(url_for('lect_login'))
        else:
            flash('invalid credential')
            return render_template('lecturer/lecturerlogin.html',lectureform=lectureform)
        

@app.route('/lecturerprofile',methods=["POST","GET"])
@csrf.exempt
def lecturerprofile():
    id=session.get('lecturer')
    if id == None:
        return redirect(url_for('lect_login'))
    else:
        if request.method == 'GET':
            lectdeets=db.session.query(Lecturers).get(id)
            return render_template ('lecturer/lecturer_profile.html',lectdeets=lectdeets)
        else:
            fullname=request.form.get('fullname')
            add=request.form.get('add')
            phone=request.form.get('phone')
            #update db 
            obj=db.session.query(Lecturers).get(id)
            obj.lecturer_fullname=fullname
            obj.lecturer_phone=phone
            obj.lecturer_add=add
            db.session.commit()
            flash('profile updated')
            return redirect(url_for('lect_profile'))

        
@app.route('/lectdashboard')
def lect_profile():
    if session.get('lecturer') != None:
        #retrieve the details of the logged in lecturer
        id=session['lecturer']
        lecdeets=db.session.query(Lecturers).get(id)
        return render_template('lecturer/lecturerdashboard.html',lecdeets=lecdeets)
    else:
        return redirect(url_for('lect_login'))


@app.route("/lecturer_studentpro")
def lecturer_studentpro():
    lectureform=LectureForm()
    if session.get('lecturer') == None:
        return render_template('lecturer/lecturerlogin.html',lectureform=lectureform)
    else:
        if request.method == 'GET':
            student = Students.query.all()
            return render_template('lecturer/view_mystudent.html',student=student)
        
@app.route('/timetable',methods=['POST','GET'])
def lect_timetable():
    if session.get('lecturer') == None:
        return render_template('lecturer/lecturerlogin.html')
    else:
        if request.method == 'GET':
            timet = Timetable.query.all()
            return render_template('lecturer/timetable.html',timet=timet)
        
@app.route('/student_attendance',methods=['POST','GET'])
def student_attendance():
    lectureform=LectureForm()
    if session.get('lecturer') == None:
        return render_template('lecturer/lecturerlogin.html')
    else:
        if request.method == 'GET':
            timetab = Timetable.query.all()
            student= Students.query.all()
            course=Course.query.all()
            return render_template('lecturer/attendance.html',course=course,timetab=timetab,student=student,lectureform=lectureform)
        else:
            timetableid = request.form.get('timetableid')
            studentid=request.form.get('studentid')
            courseid=request.form.get('courseid')
            if studentid !='' and timetableid!='' and courseid!='':
                attend = Attendance(attendance_studentid=studentid,attendance_courseid=courseid,attendance_timetableid=timetableid)
                db.session.add(attend)
                db.session.commit()
                flash("Attendance Added")
                return render_template('/lecturer/attendance.html')
            else:
                flash('Invalid credentials')
                return render_template('/lecturer/attendance.html')
   
@app.route('/reports')
def reports():
    attend = Attendance.query.all()
    return render_template('/lecturer/report.html',attend=attend)


