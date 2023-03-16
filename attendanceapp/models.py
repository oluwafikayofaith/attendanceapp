from datetime import datetime
from attendanceapp import db

class Admin(db.Model):
    admin_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username = db.Column(db.String(100),nullable=True) 
    admin_pwd=db.Column(db.String(120),nullable=True)

class Lecturers(db.Model):  
    lecturer_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    lecturer_fullname = db.Column(db.String(100),nullable=True)
    lecturer_pwd=db.Column(db.String(120),nullable=True)
    lecturer_cpwd=db.Column(db.String(120),nullable=True)
    lecturer_email = db.Column(db.String(120),nullable=False,unique=True) 
    lecturer_add=db.Column(db.String(120),nullable=True)
    lecturer_phone=db.Column(db.String(20),nullable=False)
    lecturer_status =db.Column(db.Enum('1','0'),nullable=False,server_default=('0'))

class Level(db.Model):  
    level_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    level_name = db.Column(db.String(20),nullable=True)

class Course(db.Model):  
    course_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    course_name = db.Column(db.String(20),nullable=False)
    course_code=  db.Column(db.String(100),nullable=True)
    #set foreign key
    course_levelid=db.Column(db.Integer,db.ForeignKey('level.level_id'),nullable=False)
    #set relationship
    leveldeets=db.relationship('Level',backref=('coursedeets'))

class Acadyear(db.Model):  
    acadyear_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    year_name = db.Column(db.String(20),nullable=False)
    startdate=db.Column(db.String(20),nullable=False)
    enddate=db.Column(db.String(20),nullable=False)

class Students(db.Model):  
    student_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    student_fullname = db.Column(db.String(100),nullable=True)
    student_add = db.Column(db.String(120),nullable=True)
    student_phone = db.Column(db.String(120),nullable=False)
    student_pwd = db.Column(db.String(120),nullable=True)
    student_cpwd = db.Column(db.String(120),nullable=True)
    student_email = db.Column(db.String(120), nullable=False) 
    student_status = db.Column(db.Enum('1','0'),nullable=False,server_default=('0')) 
    student_datereg = db.Column(db.DateTime(), default=datetime.utcnow)
    student_matno = db.Column(db.String(20),unique=True,nullable=False) 
    student_pix=db.Column(db.String(120),nullable=True)
    #set foreign key
    student_levelid=db.Column(db.Integer,db.ForeignKey('level.level_id'))
    #set relationship
    leveldeets=db.relationship('Level',backref=('studentdeets'))

class Timetable(db.Model):  
    timetable_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    time = db.Column(db.String(10),nullable=False)
    day= db.Column(db.String(10),nullable=False)
    #set foreign key
    timetable_acadyearid=db.Column(db.Integer,db.ForeignKey('acadyear.acadyear_id'))
    timetable_courseid=db.Column(db.Integer,db.ForeignKey('course.course_id'))
    #set relationship
    acadyeardeets=db.relationship('Acadyear',backref=('timetabledeets'))
    coursedeets=db.relationship('Course',backref=('timetabledeets'))

class Attendance(db.Model):  
    attendance_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    timein = db.Column(db.DateTime(), default=datetime.utcnow)
    #set foreign key
    attendance_studentid=db.Column(db.Integer,db.ForeignKey('students.student_id'))
    attendance_timetableid=db.Column(db.Integer,db.ForeignKey('timetable.timetable_id'))
    attendance_courseid=db.Column(db.Integer,db.ForeignKey('course.course_id'))
    #set relationship
    studentdeets=db.relationship('Students',backref=('attendancedeets'))
    timetabledeets=db.relationship('Timetable',backref=('attendancedeets'))
    coursedeets=db.relationship('Course',backref=('attendancedeets'))

class Lecturercourse(db.Model):  
    lecturercourse_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    #set foreign key
    lecturercourse_courseid=db.Column(db.Integer,db.ForeignKey('course.course_id'))
    lecturercourse_lecturerid=db.Column(db.Integer,db.ForeignKey('lecturers.lecturer_id'))
    lecturercourse_acadyearid=db.Column(db.Integer,db.ForeignKey('acadyear.acadyear_id'))
    #set relationship
    coursedeets=db.relationship('Course',backref=('lectcoursedeets'))
    lecturerdeets=db.relationship('Lecturers',backref=('lectcoursedeets'))
    acadyeardeets=db.relationship('Acadyear',backref=('lectcoursedeets'))
    


    


    


    


