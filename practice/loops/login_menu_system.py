# --- DATA ---
users = [
    {'username':'admin','password':'admin'},
    {'username':'admin1','password':'admin1'}
]

students = []
max_attempts = 3
login_success = False

# --- LOGIN ---
while max_attempts>0:
    username = input('Username:')
    password = input('Password:')

    for user in users:
        if user['username']==username and user['password']==password:
            login_success = True
            print('Login successful.')
            break

    if login_success:
        break

    max_attempts-=1
    print('Remaining login attempts:',max_attempts)

    if max_attempts == 0:
        print('Account blocked.')

if not login_success:
    exit()


# --- MENU ---
while True:
    print('--- MENU ---')
    print('1 - Add Student')
    print('2 - Find Students')
    print('3 - Quit')

    choose = input('Choose:')

    if choose == '1':
        while True:
            studentID = input('Enter Student ID:')

            if studentID == '':
                print('Wrong ID Try Again')
                continue
            if not studentID.isdigit():
                print('ID must be a number!')
                continue

            exist = False
            for student in students:
                if student['studentID']==studentID:
                    exist = True
                    break

            if exist:
                print('This ID is Already Taken.')
                continue
            break

        while True:
            studentName = input('Enter Student Name:')
            if studentName == '':
                print('Wrong Name. Try Again')
                continue
            if not studentName.isalpha():
                print('Name must contain letters only!')
                continue
            break

        while True:
            studentLastName = input('Enter Student Last Name:')
            if studentLastName == '':
                print('Wrong Last Name. Try Again')
                continue
            if not studentLastName.isalpha():
                print('Name must contain letters only!')
                continue
            break

        students.append({
            'studentID':studentID,
            'studentName':studentName,
            'studentLastName':studentLastName
        })

        print('Student added successfully.')

    elif choose == '2':
        while True:
            studentID = input('Enter Student ID:')
            if studentID == '':
                print('Invalid Input. Please try again.')
                continue
            if not studentID.isdigit():
                print('ID must be a number!')
                continue
            found = False
            for student in students:
                if student['studentID'] == studentID:
                    found = True
                    print('Student ID:',student['studentID'])
                    print('Student Name:',student['studentName'])
                    print('Student Last Name:',student['studentLastName'])
                    break
            if not found:
                print('Student not found.')
                continue
            break
    elif choose == '3':
        print('Have a nice day!')
        break


