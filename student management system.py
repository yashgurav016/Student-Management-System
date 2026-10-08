print("****************************************************************************************************")
print("===============================    STUDENT MANAGEMENT SYSTEM    ====================================")
print("****************************************************************************************************")
student = {
    1: {
        "name": "yash gurav",
        "class": "3rd year",
        "age": 20,
        "address": "malegaon",
        "phone": "+91 9823012341",
        "email": "yash.gurav@example.com",
        "department": "computer engineering",
        "cgpa": 8.75
    },
    2: {
        "name": "pavan aage",
        "class": "3rd year",
        "age": 21,
        "address": "pune",
        "phone": "+91 9823012342",
        "email": "pavan.aage@example.com",
        "department": "computer engineering",
        "cgpa": 8.40
    },
    3: {
        "name": "om gade",
        "class": "2nd year",
        "age": 19,
        "address": "kohrale",
        "phone": "+91 9823012343",
        "email": "om.gade@example.com",
        "department": "information technology",
        "cgpa": 7.90
    },
    4: {
        "name": "aslam shaikh",
        "class": "3rd year",
        "age": 20,
        "address": "nashik",
        "phone": "+91 9823012344",
        "email": "aslam.shaikh@example.com",
        "department": "computer engineering",
        "cgpa": 8.20
    },
    5: {
        "name": "basit bagwan",
        "class": "3rd year",
        "age": 20,
        "address": "baramati",
        "phone": "+91 9823012345",
        "email": "basit.bagwan@example.com",
        "department": "mechanical engineering",
        "cgpa": 8.10
    },
    6: {
        "name": "viraj chandanshive",
        "class": "2nd year",
        "age": 19,
        "address": "solapur",
        "phone": "+91 9823012346",
        "email": "viraj.chandanshive@example.com",
        "department": "civil engineering",
        "cgpa": 7.65
    },
    7: {
        "name": "mayur jadhav",
        "class": "3rd year",
        "age": 20,
        "address": "satara",
        "phone": "+91 9823012347",
        "email": "mayur.jadhav@example.com",
        "department": "electrical engineering",
        "cgpa": 8.50
    },
    8: {
        "name": "swapnil khamkar",
        "class": "2nd year",
        "age": 19,
        "address": "kolhapur",
        "phone": "+91 9823012348",
        "email": "swapnil.khamkar@example.com",
        "department": "information technology",
        "cgpa": 8.30
    },
    9: {
        "name": "krishna kadam",
        "class": "3rd year",
        "age": 20,
        "address": "sangli",
        "phone": "+91 9823012349",
        "email": "krishna.kadam@example.com",
        "department": "computer engineering",
        "cgpa": 9.10
    },
    10: {
        "name": "shekhar ganeshkar",
        "class": "2nd year",
        "age": 19,
        "address": "ahmednagar",
        "phone": "+91 9823012350",
        "email": "shekhar.ganeshkar@example.com",
        "department": "electronics & telecommunication",
        "cgpa": 7.85
    },
    11: {
        "name": "rohan jadhav",
        "class": "3rd year",
        "age": 21,
        "address": "chhatrapati sambhajinagar",
        "phone": "+91 9823012351",
        "email": "rohan.jadhav@example.com",
        "department": "mechanical engineering",
        "cgpa": 8.05
    },
    12: {
        "name": "ramesh mali",
        "class": "2nd year",
        "age": 20,
        "address": "dhule",
        "phone": "+91 9823012352",
        "email": "ramesh.mali@example.com",
        "department": "civil engineering",
        "cgpa": 7.40
    },
    13: {
        "name": "aditya shinde",
        "class": "3rd year",
        "age": 20,
        "address": "pune",
        "phone": "+91 9823012353",
        "email": "aditya.shinde@example.com",
        "department": "computer engineering",
        "cgpa": 8.90
    },
    14: {
        "name": "prathamesh pawar",
        "class": "2nd year",
        "age": 19,
        "address": "mumbai",
        "phone": "+91 9823012354",
        "email": "prathamesh.pawar@example.com",
        "department": "information technology",
        "cgpa": 8.15
    },
    15: {
        "name": "sanket deshmukh",
        "class": "3rd year",
        "age": 20,
        "address": "nagpur",
        "phone": "+91 9823012355",
        "email": "sanket.deshmukh@example.com",
        "department": "electrical engineering",
        "cgpa": 8.60
    },
    16: {
        "name": "saurabh more",
        "class": "2nd year",
        "age": 19,
        "address": "karad",
        "phone": "+91 9823012356",
        "email": "saurabh.more@example.com",
        "department": "electronics & telecommunication",
        "cgpa": 7.95
    },
    17: {
        "name": "tejas kharat",
        "class": "3rd year",
        "age": 21,
        "address": "latur",
        "phone": "+91 9823012357",
        "email": "tejas.kharat@example.com",
        "department": "computer engineering",
        "cgpa": 8.80
    },
    18: {
        "name": "aniket gawade",
        "class": "2nd year",
        "age": 19,
        "address": "nanded",
        "phone": "+91 9823012358",
        "email": "aniket.gawade@example.com",
        "department": "mechanical engineering",
        "cgpa": 7.70
    },
    19: {
        "name": "shubham jagtap",
        "class": "3rd year",
        "age": 20,
        "address": "wai",
        "phone": "+91 9823012359",
        "email": "shubham.jagtap@example.com",
        "department": "information technology",
        "cgpa": 8.45
    },
    20: {
        "name": "akash kulkarni",
        "class": "2nd year",
        "age": 19,
        "address": "pune",
        "phone": "+91 9823012360",
        "email": "akash.kulkarni@example.com",
        "department": "computer engineering",
        "cgpa": 9.25
    }
}

def student_search():

    roll_no = int(input("Enter student roll_no: "))

    if roll_no in student:
        print("\nStudent Found!")
        print("Roll Number :", roll_no)
        print("Name        :", student[roll_no]["name"])
        print("Class       :", student[roll_no]["class"])
        print("Age         :", student[roll_no]["age"])
        print("Address     :", student[roll_no]["address"])
        print("phone       :", student[roll_no]["phone"])
        print("email       :", student[roll_no]["email"])
        print("department  :", student[roll_no]["department"])
        print("cgpa        :", student[roll_no]["cgpa"])

    else:
        print("Student not found")

def add_student():
    roll_no = int(input("Enter student roll_no: "))
    if roll_no in student:
        print("Student with this roll number already exists.")
        return

    name = input("Enter student name: ")
    class_name = input("Enter student class: ")
    age = input("Enter student age: ")
    address = input("Enter student address: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    department = input("Enter student department: ")
    cgpa = input("Enter student cgpa: ")

    
    student[roll_no] = {
        "name": name,
        "class": class_name,
        "age": int(age) if age.isdigit() else age,
        "address": address,
        "phone":phone,
        "email":email,
        "department":department,
        "cgpa":cgpa
    }
    print("Student added successfully.")

def show_all_students():
    if not student:
        print("No students available.")
        return

    print("\nAll Students:")
    for roll_no, info in student.items():
        print("-" * 40)
        print("Roll Number :", roll_no)
        print("Name        :", info["name"])
        print("Class       :", info["class"])
        print("Age         :", info["age"])
        print("Address     :", info["address"])
        print("phone       :", info["phone"])
        print("email       :", info["email"])
        print("department  :", info["department"])
        print("cgpa        :", info["cgpa"])
    print("-" * 40)


# Do not call searches immediately; they will be invoked from the menu below

teacher = {
    "101": {
        "name": "ajit bansode",
        "subject": "maths",
        "class":"10th",
        "experience": "10 years",
    },
    "102": {
            "name": "yash jadhav",
            "subject": "che",
            "class":"10th",
            "experience": "5 years",
        },
        "103": {
                "name": "akansha bhise",
                "subject": "phy",
                "class":"12th",
                "experience": "11 years",
            },
    }
def teacher_search():
    teacher_id = input("Enter teacher id: ")

    if teacher_id in teacher:
        print("\nTeacher Found!")
        print("Teacher ID   :", teacher_id)
        print("Name         :", teacher[teacher_id]["name"])
        print("Subject      :", teacher[teacher_id]["subject"])
        print("Class        :", teacher[teacher_id]["class"])
        print("Experience   :", teacher[teacher_id]["experience"])
    else:
        print("Teacher not found")

# teacher_search() will be called from the menu


worker = {
    "1001": {
        "name": "pawan aage",
        "section": "A",
        "shift": "12 hours",
        "holiday": "sunday",
    },
    "1002": {
        "name": "viraj shive",
        "section": "b",
        "shift": "8 hours",
        "holiday": "monday",
    },
    "1003": {
        "name": "rohit pawar",
        "section": "c",
        "shift": "6 hours",
        "holiday": "saturday",
    },
}


def worker_search():
    worker_id = input("Enter worker id: ")

    if worker_id in worker:
        print("\nWorker Found!")
        print("Worker ID   :", worker_id)
        print("Name        :", worker[worker_id]["name"])
        print("Section     :", worker[worker_id]["section"])
        print("Shift       :", worker[worker_id]["shift"])
        print("Holiday     :", worker[worker_id]["holiday"])
    else:
        print("Worker not found")


# worker_search() will be called from the menu


while True:
    print("1.student")
    print("2.add student")
    print("3.show all students")
    print("4.teacher")
    print("5.worker")
    print("6.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        student_search()
    elif choice == '2':
        add_student()
    elif choice == '3':
        show_all_students()
    elif choice == '4':
        teacher_search()
    elif choice == '5':
        worker_search()
    elif choice == '6':
        print("Exiting...") 
        break
    else:
        print("Invalid choice, try again.")


