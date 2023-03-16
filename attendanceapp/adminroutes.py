from flask import render_template,redirect,flash,session,request,url_for
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from attendanceapp import app,db
from attendanceapp.models import Admin,Lecturercourse,Course,Lecturers,Level,Acadyear,Timetable,Attendance,Students
from attendanceapp.forms import AdForm
from attendanceapp import csrf




@app.route("/admin/",methods=['POST','GET'])
def admin_home():
        adform=AdForm()
        if request.method == "GET":
            return render_template('/admin/adminreg.html',adform=adform)
        else:
            if adform.validate_on_submit():
                #retrieve data coming from the form
                username = request.form.get('username')
                password = request.form.get('password')
                hashed_pwd = generate_password_hash(password)
                #insert into database
                ad = Admin(admin_username=username,admin_pwd=hashed_pwd)
                db.session.add(ad)
                db.session.commit()
                flash("Registration Successful.")
                return render_template('/admin/index.html', adform=adform)
            else:
                flash("Username and password must be applied")
                return redirect(url_for('admin_home'))

@app.route("/admin/login/",methods=['POST','GET'])
def admin_login():
    adform = AdForm()
    if request.method == 'GET':
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        #query to confirm the login credentials
        addeets=db.session.query(Admin).filter(Admin.admin_username==username).first()
        if addeets != None:
            pwd_indb = addeets.admin_pwd 
            check = check_password_hash(pwd_indb,password) 
            if check== True:
                id= addeets.admin_id
                session['adminloggedin']=id
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))  
        else:
            flash('Invalid credentials')
            return redirect(url_for('admin_login'))
        
@app.route('/admin/add_level', methods=['POST','GET'])
@csrf.exempt
def add_level():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        if request.method == 'GET':
            return render_template('/admin/add_level.html')
        else:
            addlevel = request.form.get('addlevel')
            if addlevel !='':
                lev = Level(level_name=addlevel)
                db.session.add(lev)
                db.session.commit()
                flash("Level Added")
                return render_template('/admin/add_level.html')
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))
       
    
@app.route("/admin/academicyear", methods=['POST','GET'])
def academicyear():
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html')
    else:
        if request.method == 'GET':
            deetacad = Acadyear.query.all()
            return render_template('/admin/academicyear.html',deetacad=deetacad)
        else:
            startdate= request.form.get('startdate')
            enddate=request.form.get('enddate')
            yearname=request.form.get('yearname')
            if yearname !='' and startdate!='' and enddate !='':
                acad = Acadyear(year_name=yearname,startdate=startdate,enddate=enddate)
                db.session.add(acad)
                db.session.commit()
                flash("Year Added")
                return render_template('/admin/academicyear.html')
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))


# @app.route("/admin/attendance")
# def attendancee():
#     adform=AdForm()
#     if session.get('adminloggedin')== None:
#         return render_template('/admin/adminlogin.html',adform=adform)
#     else:
#         if request.method == 'Get':
#             student= db.session.query(Students).all()
#             timetable=db.session.query(Timetable).all()
#             deetattend = Attendance.query.all()
#             return render_template('/admin/attendance.html',adform=adform,deetattend=deetattend,student=student,timetable=timetable)
#         else:
#             studentid=request.form.get('studentid')
#             timetableid=request.form.get('timetableid')
#             timein=request.form.get('timein')
#             if studentid !='' and timetableid!='' and timein !='':
#                 attend = Attendance(timein=timein,attendance_studentid=studentid,attendance_timetableid=timetableid)
#                 db.session.add(attend)
#                 db.session.commit()
#                 flash("Attendance Added")
#                 return render_template('/admin/attendance.html')
#             else:
#                 flash('Invalid credentials')
#                 return redirect(url_for('admin_login'))

@app.route("/admin/lecturer_course", methods=['POST','GET'])
def lecturer_course():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        if request.method == 'GET':
            lecturer = db.session.query(Lecturers).all()
            course= db.session.query(Course).all()
            acadyear=db.session.query(Acadyear).all()
            lecturercoursedeets=Lecturercourse.query.all()
            return render_template('/admin/lecturer_course.html',lecturercoursedeets=lecturercoursedeets,adform=adform,course=course,acadyear=acadyear,lecturer=lecturer)
        else:
            lecturerid = request.form.get('lecturerid')
            courseid= request.form.get('courseid')
            academicyearid=request.form.get('academicyearid')
            if academicyearid !='' and courseid!='' and lecturerid !='':
                lecturercourse = Lecturercourse(lecturercourse_lecturerid=lecturerid,lecturercourse_courseid=courseid,lecturercourse_acadyearid=academicyearid)
                db.session.add(lecturercourse)
                db.session.commit()
                flash("Course Added")
                return render_template('/admin/lecturer_course.html')
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))
      
     

@app.route("/admin/add_course", methods=['POST','GET'])
def add_course():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        if request.method == 'GET':
            level = Level.query.all()
            deetcourse = Course.query.all()
            return render_template('/admin/add_course.html',deetcourse=deetcourse,adform=adform,level=level)
        else:
            coursecode = request.form.get('coursecode')
            coursetitle= request.form.get('coursetitle')
            levelid=request.form.get('levelid')
            if coursecode !='' and coursetitle!='' and levelid !='':
                cos = Course(course_name=coursetitle,course_code=coursecode,course_levelid=levelid)
                db.session.add(cos)
                db.session.commit()
                flash("Course Added")
                return render_template('/admin/add_course.html')
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))
       

@app.route('/admin/timetable',methods=['POST','GET'])
def timetable():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        if request.method == 'GET':
            acadyear = db.session.query(Acadyear).all()
            course = db.session.query(Course).all()
            timet = Timetable.query.all()
            return render_template('/admin/timetable.html',adform=adform,timet=timet,acadyear=acadyear,course=course)
        else:
            time = request.form.get('time')
            day=request.form.get('day')
            courseid= request.form.get('courseid')
            acadyearid=request.form.get('acadyearid')
            if courseid !='' and time!='' and acadyearid !='':
                time_table = Timetable(time=time,day=day,timetable_acadyearid=acadyearid,timetable_courseid=courseid)
                db.session.add(time_table)
                db.session.commit()
                flash("Timetable Added")
                return render_template('/admin/timetable.html')
            else:
                flash('Invalid credentials')
                return redirect(url_for('admin_login'))
            
@app.route('/admin/reports')
def attendance_reports():
    attend = Attendance.query.all()
    return render_template('/admin/reports.html',attend=attend)


@app.route("/admin/studentpro")
def admin_studentpro():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/adminlogin.html',adform=adform)
    else:
        if request.method == 'GET':
            student = Students.query.all()
            return render_template('/admin/admin_studentpro.html',adform=adform,student=student)

@app.route("/admin/lecturerpro")
def admin_lecturerpro():
    adform=AdForm()
    if session.get('adminloggedin') == None:
        return render_template('/admin/admin_lecturerpro.html',adform=adform)
    else:
        if request.method == 'GET':
            lecturer = Lecturers.query.all()
            return render_template('/admin/admin_lecturerpro.html',adform=adform,lecturer=lecturer)



@app.route("/admin/dashboard")
def admin_dashboard():
    adform=AdForm()
    return render_template('admin/index.html',adform=adform)
     
@app.route("/admin/logout")
def admin_logout():
    if session.get('adminloggedin')!=None:
        session.pop('adminloggedin',None)
    
    return redirect("/admin/login")


@app.route('/admin/lecturercourse/delete/<id>')
def delete_lectcourse(id):
    lectcourseobj = Lecturercourse.query.get_or_404(id)
    db.session.delete(lectcourseobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('lecturer_course'))

@app.route('/admin/acadyear/delete/<id>')
def delete_acadyear(id):
    acadyearobj = Acadyear.query.get_or_404(id)
    db.session.delete(acadyearobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('academicyear'))


@app.route('/admin/timetable/delete/<id>')
def delete_timetable(id):
    timetableobj = Timetable.query.get_or_404(id)
    db.session.delete(timetableobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('timetable'))

@app.route('/admin/course/delete/<id>')
def delete_course(id):
    courseobj = Course.query.get_or_404(id)
    db.session.delete(courseobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('add_course'))

@app.route('/admin/studentpro/delete/<id>')
def delete_studentpro(id):
    studentobj = Students.query.get_or_404(id)
    db.session.delete(studentobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('admin_studentpro'))

@app.route('/admin/lecturerpro/delete/<id>')
def delete_lecturerpro(id):
    lecturerobj = Lecturers.query.get_or_404(id)
    db.session.delete(lecturerobj)
    db.session.commit()
    flash('Successfully deleted')
    return redirect(url_for('admin_lecturerpro'))






































@app.errorhandler(404)
def pagenotfound(error):
    #return render_template('error404.html',error=error),404
    return 'error'

@app.errorhandler(500)
def internalerror(error):
    '''For you to see this in action, ensure the debug mode is set to false'''
    return "sorry, an error occured",500
