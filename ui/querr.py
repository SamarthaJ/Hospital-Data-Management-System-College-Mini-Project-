# This file contains all the querries that are used in the UI_code
import login_SQL as li

db=li.create_connection()
mycursor=db.cursor()

#used to get the number of patients
def no_of_patients():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) FROM affiliated WHERE status = 'A'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#gives the count of discharged patients
def discharged_patients():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) FROM affiliated WHERE status = 'D'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#gives the count of patients in ICU
def icu_patients():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) AS patient_count FROM affiliated WHERE status = 'ICU'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#gives the count of deceased patients
def deceased_patients():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) FROM affiliated WHERE status = 'E'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#used to get the list of doctors by thier department
def doctors_list_by_dept():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute(f"SELECT name,emp_id,role FROM employee where role='Doctor' or role='Surgon'")
    a=[]
    for x in mycursor:
        # clean_string = str(x).replace("'", "").replace("(","").replace(",","").replace(")","")
        a.append(x)

    return a
    
#Used to get the count of doctors
def doc_count():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) AS doctor_count FROM employee where role='Doctor' or role='Surgon'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#Used to get the count of nurses
def nurse_count():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(*) AS nurse_count FROM employee where role='Nurse'")
    for x in mycursor:
        val=x
    vali = val[0]
    return vali

#list that has all departments in the hospital. Used for the drop down menu in doctors tab
def dept_list():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT DEPT_NAME FROM DEPARTMENT")
    arr=[]
    for x in mycursor:
        clean_string = str(x).replace("'", "").replace("(","").replace(")","").replace(",","")
        arr.append(clean_string)
    return arr

#Gives the no of patients present in the hospital
def curr_patients():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT COUNT(DISTINCT p_id) AS total_patients_present FROM affiliated WHERE DOA <= CURDATE() AND (DOD >= CURDATE() OR DOD IS NULL)")
    for x in mycursor:
        val=str(x).replace("(","").replace(",","").replace(")","")
    return int(val)

#gives revenue collected today
def revenue():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT SUM(p.cost) AS total_amount_collected FROM undergo u JOIN procedur p ON u.pro_id = p.pro_id WHERE u.sedu_date = CURDATE()")
    for x in mycursor:
        val=str(x).replace("(","").replace(",","").replace(")","").replace("'","").replace("Decimal","")
    if val == "None":
        val = "0"
    else:
        return val

def appointment_lst():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("SELECT p.name AS patient_name, d.name, a.time AS appointment_time FROM appointment a JOIN patient p ON a.p_id = p.p_id JOIN employee d ON a.emp_id = d.emp_id ")
    arr=[list(i) for i in mycursor]
    return arr

def avaliable_rooms():
    db=li.create_connection()
    mycursor=db.cursor()
    a=[]
    mycursor.execute("SELECT r.r_no FROM Room r LEFT JOIN affiliated a ON r.r_no = a.r_no WHERE a.r_no IS NULL;")
    for x in mycursor:
        val=x[0]
        a.append(val)
    return(a)

def block_aval():
    db=li.create_connection()
    mycursor=db.cursor()
    a=[]
    mycursor.execute("SELECT DISTINCT b_name FROM Room;")
    for x in mycursor:
        val=x[0]
        a.append(val)
    return a

def add_patient(pid,name,aadhar,dob,mobile,email,address,insu_id,sex):
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute(f"insert into patient values('{pid}','{name}','{aadhar}','{dob}','{mobile}','{email}','{address}','{insu_id}','{sex}')")
    db.commit()

def patientInfo():
    db=li.create_connection()
    mycursor=db.cursor()
    mycursor.execute("select name,p_id,Insurence_id,mobile from patient")
    arr=[list(i) for i in mycursor]
    return arr
