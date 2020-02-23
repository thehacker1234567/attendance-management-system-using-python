from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):

    name=StringField('Name of the Student:')
    sem=IntegerField('semester')
    dept=StringField('Department')
    st_phno=IntegerField('Student phno:')
    pa_phno=IntegerField('parent phno')
    submit=SubmitField('Add Student')

class AddTeacherForm(FlaskForm):


    tc_name = StringField("name of the teacher: ")
    tc_dept=StringField("department: ")
    submit = SubmitField('Add Teacher')


class AddSubjectForm(FlaskForm):


    sem3 = IntegerField("semester of the student: ")

    dept3=StringField("department:")

    sub_name=StringField("subject:")
    teacher_name=StringField("teacher name:")
    submit = SubmitField('Add Subject')

class AddAttendanceForm(FlaskForm):


    stud_usn = IntegerField("usn of the student: ")
    date=IntegerField("Date: ")
    status=StringField("present/absent:")
    dept2=StringField("department:")
    sem2=IntegerField("semester:")

    submit = SubmitField('Add Attendance')

class AddReportForm(FlaskForm):


    stu_usn = IntegerField("usn of the student: ")
    st2_name=StringField("name of student:")
    dept4=StringField("department:")
    sem4=IntegerField("semester:")
    attpercentage=IntegerField("attendance percentage:")
    submit = SubmitField('Add Report')



class DelForm(FlaskForm):
    usn=IntegerField('usn of student to remove:')

    submit=SubmitField('Remove Student')
