# Student Information System
# Version: v0.3
# Features:
# - Student lookup by ID
# - Formatted output
# - Average grade calculation
# - Pass / Fail status

students = {
    101:{
        'name':'Michael',
        'last_name':'Anderson',
        'email':'admin1@gmail.com',
        'faculty':'Engineering',
        'department':'Computer Engineering',
        'advisor':'example1',
        'class_year':1,
        'grades':{
            'midterm':[70,65,90],
            'finals':[65,80,40]
        }

    },
    102:{
        'name':'Emily',
        'last_name':'Carter',
        'email':'admin2@gmail.com',
        'faculty':'Science',
        'department':'Physics',
        'advisor':'example2',
        'class_year':3,
        'grades':{
            'midterm':[70,65,85],
            'finals':[75,60,90]
        }
    },
    103:{
        'name':'Sarah',
        'last_name':'Williams',
        'email':'admin3@gmail.com',
        'faculty':'Economics and Administrative Sciences',
        'department':'Economics',
        'advisor':'example3',
        'class_year':2,
        'grades':{
            'midterm':[80,70,90],
            'finals':[70,70,85]
        }
    },
    104:{
        'name':'Alexander',
        'last_name':'Brown',
        'email':'admin4@gmail.com',
        'faculty':'Engineering',
        'department':'Mechanical Engineering',
        'advisor':'example4',
        'class_year':1,
        'grades':{
            'midterm':[45,60,50],
            'finals':[70,75,65]
        }
    },
    105:{
        'name':'Ethan',
        'last_name':'Foster',
        'email':'admin5@gmail.com',
        'faculty':'Arts and Humanities',
        'department':'Philosophy',
        'advisor':'example5',
        'class_year':4,
        'grades':{
            'midterm':[70,85,80],
            'finals':[80,90,75]
        }
    }
}

student_id = int(input('Student ID: '))
student = students.get(student_id)

if student:
    print('Student Information')
    print('-------------------')
    print('Name: ', student['name'],student['last_name'])
    print('Faculty: ', student['faculty'])
    print('Department:', student['department'])
    print('Class: ', student['class_year'])
    print('Advisor: ', student['advisor'])
    #Ortalama Hesabi
    midterms = student['grades']['midterm']
    finals = student['grades']['finals']

    midterm_avg = round((midterms[0]+midterms[1]+midterms[2]) / 3,2)
    final_avg = round((finals[0]+finals[1]+finals[2]) / 3,2)
    overall_avg = round((midterm_avg+final_avg) / 2,2)

    print('Student Grades')
    print('--------------')
    print('Midterm Average:', midterm_avg)
    print('Final Average:', final_avg)
    print('Overall Average:', overall_avg)

    if overall_avg >=60:
        print('Status: PASSED')
    else:
        print('Status: FAILED')
else:
    print('Student not found.')


