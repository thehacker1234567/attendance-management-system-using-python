import os
from forms import AddForm,DelForm,AddTeacherForm,AddAttendanceForm,AddSubjectForm,AddReportForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask(__name__,template_folder="templates1")

app.config['SECRET_KEY']='mysecretkey1'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)
Migrate(app,db)

class students(db.Model):

    __tablename__='STUDENTS'
    usn=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    sem=db.Column(db.Integer)
    dept=db.Column(db.Text)
    st_phno=db.Column(db.Integer)
    pa_phno=db.Column(db.Integer)
    att1=db.relationship('attendance',backref='Students',uselist=False)




    def __init__(self,name,sem,dept,st_phno,pa_phno):
        self.name=name
        self.sem=sem
        self.dept=dept
        self.st_phno=st_phno
        self.pa_phno=pa_phno

    def __repr__(self):
        return f"name of student: {self.name}, semester: {self.sem}, department: {self.dept}, student phno: {self.st_phno}, parent phno: {self.pa_phno} "

class teacher(db.Model):

    __tablename__='TEACHERS'
    tc_id=db.Column(db.Integer,primary_key=True)
    tc_name=db.Column(db.Text)
    tc_dept=db.Column(db.Text)
    tc1=db.relationship('subject',backref='Teacher',uselist=False)


    def __init__(self,tc_name,tc_dept):
        self.tc_name=tc_name
        self.tc_dept=tc_dept

    def __repr__(self):
        return f"name of teacher: {self.tc_name}, department: {self.tc_dept}"


class subject(db.Model):

    __tablename__='SUBJECT'
    sub_id=db.Column(db.Integer,primary_key=True)
    sem3=db.Column(db.Integer)
    dept3=db.Column(db.Text)
    sub_name=db.Column(db.Text)
    teacher_name=db.Column(db.Text,db.ForeignKey('TEACHERS.tc_name'))


    def __init__(self,sem3,dept3,sub_name,teacher_name):
        self.sem3=sem3
        self.dept3=dept3
        self.sub_name=sub_name
        self.teacher_name=teacher_name

    def __repr__(self):
        return f"subid:{self.sub_id},semester:{self.sem3},department:{self.dept3},subject:{self.sub_name},teacher:{self.teacher_name}"

class attendance(db.Model):

    __tablename__='ATTENDANCE'
    stud_usn=db.Column(db.Integer,db.ForeignKey('STUDENTS.usn'))
    att_id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.Integer)
    status=db.Column(db.Text)
    dept2=db.Column(db.Text)
    sem2=db.Column(db.Integer)


    def __init__(self,stud_usn,date,status,dept2,sem2):
        self.stud_usn=stud_usn
        self.date=date
        self.status=status
        self.dept2=dept2
        self.sem2=sem2


    def __repr__(self):
        return f"usn:{self.stud_usn},date: {self.date},status: {self.status},department: {self.dept2},semester: {self.sem2}"


class report(db.Model):

    __tablename__='REPORTS'

    stu_usn=db.Column(db.Integer,db.ForeignKey('STUDENTS.usn'))
    st2_name=db.Column(db.Text,db.ForeignKey('STUDENTS.name'))
    dept4=db.Column(db.Text)
    sem4=db.Column(db.Integer,db.ForeignKey('STUDENTS.sem'))

    attpercentage=db.Column(db.Integer,primary_key=True)

    def __init__(self,stu_usn,st2_name,dept4,sem4,attpercentage):
        self.stu_usn=stu_usn
        self.st2_name=st2_name
        self.dept4=dept4
        self.sem4=sem4

        self.attpercentage=attpercentage

    def __repr__(self):
        return f"usn:{self.stu_usn},name:{self.st2_name},department:{self.dept4},semester:{self.sem4},atteperc:{self.attpercentage}"




@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_student():
    form=AddForm()

    if form.validate_on_submit():
        name=form.name.data
        sem=form.sem.data
        dept=form.dept.data
        st_phno=form.st_phno.data
        pa_phno=form.pa_phno.data

        new_stud=students(name,sem,dept,st_phno,pa_phno)

        db.session.add(new_stud)
        db.session.commit()



    return render_template('add.html',form=form)


@app.route('/teacher', methods=['GET', 'POST'])
def add_teacher():

    form = AddTeacherForm()

    if form.validate_on_submit():
        tc_name = form.tc_name.data
        tc_dept=form.tc_dept.data

        new_teacher =teacher(tc_name,tc_dept)
        db.session.add(new_teacher)
        db.session.commit()



    return render_template('teacher.html',form=form)


@app.route('/subject', methods=['GET', 'POST'])
def add_subject():

    form = AddSubjectForm()

    if form.validate_on_submit():
        sem3 = form.sem3.data
        dept3=form.dept3.data
        sub_name=form.sub_name.data
        teacher_name=form.teacher_name.data


        new_subject =subject(sem3,dept3,sub_name,teacher_name)
        db.session.add(new_subject)
        db.session.commit()



    return render_template('subject.html',form=form)

@app.route('/attendance', methods=['GET', 'POST'])
def add_attendance():

    form = AddAttendanceForm()

    if form.validate_on_submit():
        stud_usn = form.stud_usn.data
        date=form.date.data
        status=form.status.data
        dept2=form.dept2.data
        sem2=form.sem2.data



        new_attendance =attendance(stud_usn,date,status,dept2,sem2)
        db.session.add(new_attendance)
        db.session.commit()



    return render_template('attendance.html',form=form)

@app.route('/list')
def list_stud():

    STUDENTS = students.query.all()
    return render_template('list.html', STUDENTS=STUDENTS)

@app.route('/listteacher')
def list_teach():

    TEACHERS = teacher.query.all()
    return render_template('listteacher.html', TEACHERS=TEACHERS)

@app.route('/listsubject')
def list_sub():

    SUBJECT = subject.query.all()
    return render_template('listsubject.html', SUBJECT=SUBJECT)

@app.route('/listreport')
def list_rep():

    REPORTS = report.query.all()
    return render_template('listreport.html', REPORTS=REPORTS)

@app.route('/listattendance')
def list_att():

    ATTENDANCE = attendance.query.all()
    return render_template('listattendance.html', ATTENDANCE=ATTENDANCE)

@app.route('/query1')
def list_query1():


    STUDENTS1=students.query.group_by(students.name).filter(students.dept=='ise').all()
    return render_template('query1.html',STUDENTS1=STUDENTS1)

@app.route('/query2')
def list_query2():


    SUBJECT1=subject.query.group_by(subject.sub_id).filter(subject.dept3=='ise').filter(subject.sem3==5).all()
    return render_template('query2.html',SUBJECT1=SUBJECT1)

@app.route('/query3')
def list_query3():


    REPORTS1=report.query.filter(report.attpercentage<85).filter(report.dept4=='ise')
    return render_template('query3.html',REPORTS1=REPORTS1)

@app.route('/query4')
def list_query4():


    query4=subject.query.filter(teacher.tc_dept==subject.dept3).filter(subject.sub_name=='me')
    return render_template('query4.html',query4=query4)

@app.route('/query5')
def list_query5():
    query5=students.query.filter(students.usn==attendance.stud_usn).filter(attendance.status=='present').filter(attendance.date==410)
    return render_template('query5.html',query5=query5)

@app.route('/delete', methods=['GET', 'POST'])
def del_stud():

    form = DelForm()

    if form.validate_on_submit():
        usn = form.usn.data
        stud = students.query.get(usn)
        db.session.delete(stud)
        db.session.commit()

        return redirect(url_for('list_stud'))
    return render_template('delete.html',form=form)

@app.route('/report', methods=['GET', 'POST'])
def add_reports():

    form = AddReportForm()

    if form.validate_on_submit():
        stu_usn = form.stu_usn.data
        st2_name=form.st2_name.data
        dept4=form.dept4.data
        sem4=form.sem4.data

        attpercentage=form.attpercentage.data



        new_report =report(stu_usn,st2_name,dept4,sem4,attpercentage)
        db.session.add(new_report)
        db.session.commit()



    return render_template('report.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
