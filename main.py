# from academic import Academic
# from admin import Admin

class Employee:
    def __init__(self, employeeID: str, name: str, dateOfBith: str, materialStatus: str,
                 numberOfChild: str, gender: str, email: str, mobile: str, fax: str, type: str, status: str,
                 department: str, startingTime: str, basicSalary: str, healthInsurance: bool):
        self.employeeID = employeeID
        # id.isdigit() && len(id)==5
        self.name = name
        self.dateOfBith = dateOfBith
        self.materialStatus = materialStatus
        self.numberOfChild = numberOfChild
        self.gender = gender
        self.contantInformation = email + ' ' + mobile + ' ' + fax
        self.type = type
        self.status = status
        self.department = department
        self.startingTime = startingTime
        self.basicSalary = basicSalary
        self.healthInsurance = healthInsurance


class Admin(Employee):
    def __init__(self, employeeID: str, name: str, dateOfBith: str, materialStatus: str,
                 numberOfChild: str, gender: str, email: str, mobile: str, fax: str, type: str, status: str,
                 department: str, startingTime: str, basicSalary: str, healthInsurance: bool):
        Employee.__init__(self, employeeID, name, dateOfBith, materialStatus,
                          numberOfChild, gender, email, mobile, fax, type, status,
                          department, startingTime, basicSalary, healthInsurance)

        self.vacation = {}


class Academic(Employee):
    def __init__(self, employeeID: str, name: str, dateOfBith: str, materialStatus: str,
                 numberOfChild: str, gender: str, email: str, mobile: str, fax: str, type: str, status: str,
                 department: str, startingTime: str, basicSalary: str, healthInsurance: bool):
        Employee.__init__(self, employeeID, name, dateOfBith, materialStatus,
                          numberOfChild, gender, email, mobile, fax, type, status,
                          department, startingTime, basicSalary, healthInsurance)

        self.experience = {}


# -------------------------------------------------------------------------------------
def readAcademic(Records: list):  # Academic.txt
    while True:
        try:
            file = input("give here the file name (Academic.txt) of Academic data : ")
            f = open(file, "r")
            break
        except IOError:
            print("{File is not existed}  please try again")

    for line in f.read().split('\n')[1:]:  # to remove the first line in the file
        id = line.split('; ')[0]
        semesterYear = line.split('; ')[1] + '_' + line.split('; ')[2]
        cources = line.split('; ')[3]

        for x in Records:
            if x.employeeID == id:
                x.experience[semesterYear] = cources
    return Records


def readGeneral(Records: list):  # GAttributes.txt
    while True:
        try:
            file = input("give here the file name (GAttributes.txt) of general data : ")
            f = open(file, "r")
            break
        except IOError:
            print("{File is not existed}  please try again")

    for line in f.read().split("\n")[1:]:
        employeeID = line.split('; ')[0]
        name1 = line.split('; ')[1].split(',')[0]
        name2 = line.split('; ')[1].split(',')[1]
        name3 = line.split('; ')[1].split(',')[2]
        dateOfBith = line.split('; ')[2]
        materialStatus = line.split('; ')[3]
        numberOfChilds = line.split('; ')[4]
        gender = line.split('; ')[5]
        if gender == "Male ":
            gender = "Male"
        elif gender == "Female ":
            gender = "Female"
        email = line.split('; ')[6].split(', ')[0]
        mobile = line.split('; ')[6].split(', ')[1]
        fax = line.split('; ')[6].split(', ')[2]
        type = line.split('; ')[7]
        status = line.split('; ')[8]
        department = line.split('; ')[9]
        startingTime = line.split('; ')[10]
        basicSalary = line.split('; ')[11]
        healthInsurance = line.split('; ')[12]
        if healthInsurance == "true":
            health = True
        else:
            health = False

        if type == "Academic":
            x = Academic(employeeID=employeeID, name=name1 + ' ' + name2 + ' ' + name3, dateOfBith=dateOfBith,
                         materialStatus=materialStatus, numberOfChild=numberOfChilds, gender=gender, email=email,
                         mobile=mobile, fax=fax, type=type, status=status, department=department,
                         startingTime=startingTime, basicSalary=basicSalary, healthInsurance=health)
        else:
            x = Admin(employeeID=employeeID, name=name1 + ' ' + name2 + ' ' + name3, dateOfBith=dateOfBith,
                      materialStatus=materialStatus, numberOfChild=numberOfChilds, gender=gender, email=email,
                      mobile=mobile, fax=fax, type=type, status=status, department=department,
                      startingTime=startingTime, basicSalary=basicSalary, healthInsurance=health)

        Records.append(x)
    return Records


def readAdmin(Records: list):
    while True:
        try:
            file = input("put the file name of Admin data (Administrative.txt) : ")
            f = open(file, "r")
            break
        except IOError:
            print(" {File is not existed}  please try again")

    for line in f.read().split('\n')[1:]:
        id = line.split("; ")[0]
        year = line.split("; ")[1]
        numberOfVacationDays = line.split("; ")[2]

        for x in Records:
            if x.employeeID == id:
                x.vacation[year] = numberOfVacationDays

    return Records


# ------------------------------------------------------------------------------------

# this method to check if its 5 digits
def isId(id: str):
    if len(id) == 5 and id.isdigit():
        return True
    else:
        return False


# its only check if its exist
def isIdExist(id: str, Records: list):
    for x in Records:
        if x.employeeID == id:
            return True
    return False


# this will check the id if its 5 digit and if its existed in our Employees information or not
def isEmployeeID(employeeID: str):
    if not (employeeID.isdigit() and len(employeeID) == 5):
        return False
    elif isIdExist(id=employeeID, Records=Records):
        return False
    else:
        return True  #


def employeeID():
    while True:
        employeeID = input("put here the employeeID ... ")
        if isEmployeeID(employeeID):
            break
        else:
            print("You have Entered a Wrong Id number or its already existed . . .")
    return employeeID


# -----------------------------------------------------------------------------------------------
def isName(name: str):
    if not name.isalpha():
        return False
    else:
        return True


def name(i: int):
    while True:
        if i == 1:
            s = "first"
        elif i == 2:
            s = "second"
        else:
            s = "last"
        name = input(f"put here the {s} name ... ")
        if isName(name=name):
            return name
        else:
            print("You have entered a wrong name please enter only characters")


# ----------------------------------------------------------------------------------------------
def isMaterialStatus(materialStatus: str):
    if not (
            materialStatus.lower() == "single" or materialStatus.lower() == "married" or materialStatus.lower() == "maried"):
        return False
    else:
        return True


def materialStatus():
    while True:
        materialStatus = input("put here the material Status  single or married")
        if isMaterialStatus(materialStatus):
            return materialStatus
        else:
            print("material Status must be single or married please try again ..")


# ----------------------------------------------------------------------------------------------
def isNumberOfChilds(numberOfChilds: str):
    if not numberOfChilds.isdigit():
        return False
    else:
        return True


def numberOfChilds():
    while True:
        numberOfChilds = input("put here the number of Children :")
        if isNumberOfChilds(numberOfChilds):
            return numberOfChilds
        else:
            print("you must give a number please try again ...")


# ----------------------------------------------------------------------------------------------
def isGender(gender: str):
    while True:
        if (gender.lower() == "male" or gender.lower() == "female"):
            return True
        else:
            return False


def gender():
    while True:
        gender = input("put here the gender  male or female")
        if isGender(gender):
            return gender
        else:
            print("gender  must be male or female please try again ..")


# ----------------------------------------------------------------------------------------------
def isType(type: str):
    if not (type == "academic" or type == "administrative"):
        return False
    else:
        return True


def type():
    while True:
        type = input("put here the type   academic or administrative")
        if isType(type):
            return type
        else:
            print("type  must be academic or administrative please try again ..")


# ----------------------------------------------------------------------------------------------
def isStatus(status: str):
    if not (status.lower() == "full-time" or status.lower() == "part-time" or status.lower() == "left-university"):
        return False
    else:
        return True


def status():
    while True:
        status = input("put here the  Status  full-time or part-time or left-university")
        if isStatus(status):
            return status
        else:
            print("status  must be full-time or part-time or left-university please try again ..")


# ----------------------------------------------------------------------------------------------
def isBasicSalary(basicSalary: str):
    if not basicSalary.isdigit():
        return False
    else:
        return True


def basicSalary():
    while True:
        basicSalary = input("put here the Basic salary")
        if isBasicSalary(basicSalary):
            return basicSalary
        else:
            print("you must give a number please try again ...")


# ----------------------------------------------------------------------------------------------
def isHealthInsurance(healthInsurance: str):
    if healthInsurance == "true":
        return True
    elif healthInsurance == "false":
        return True
    else:
        return False


def healthInsurance():
    while True:
        healthInsurance = input(
            "for healthInsurance put {true}  if the employee is enrolled with the university health insurance Otherwise, write {false} ")
        if healthInsurance == "true":
            return True

        elif healthInsurance == "false":
            return False

        else:
            print("you have entered unvalid input please try again")


# ----------------------------------------------------------------------------------------------

# its will search for the Employee by hi ID and return his Index in the Records[index] List
def findEmployee(Records: list, id: str):
    i = 0
    for x in Records:
        if x.employeeID == id:
            return i
        i += 1
    print("the id is not existed")
    return None


# print every thing in general Information
def show(Records: list):
    for x in Records:
        print(f"employeeID = {x.employeeID} \n"
              f"name= {x.name} \n"
              f"dateOfBith= {x.dateOfBith} \n"
              f"materialStatus= {x.materialStatus} \n"
              f"numberOfChild= {x.numberOfChild} \n"
              f"gender= {x.gender} \n"
              f"contantInformation= {x.contantInformation} \n"
              f"type= {x.type} \n"
              f"status= {x.status} \n"
              f"department= {x.department} \n"
              f"startingTime= {x.startingTime} \n"
              f"basicSalary= {x.basicSalary} \n"
              f"healthInsurance= {x.healthInsurance} \n"
              f"-------------------------------------\n")


# ----------------------------------------------------------------------------------------------
def numberOfAcademiv(Records: list):
    num = 0
    for x in Records:
        if x.type == "Academic":
            num += 1
    return num


def numberOfFullTime(Records: list):
    num = 0
    for x in Records:
        if x.status.lower() == "full-time" or x.status.lower() == "full-time ":
            num += 1
    return num


# ----------------------------------------------------------------------------------------------
def numOfMale(Records: list):
    num = 0
    for x in Records:

        if x.gender == "Male":
            num += 1
    return num


def numOfFemale(Records: list):
    num = 0
    for x in Records:
        if x.gender == "Female":
            num += 1
    return num


def numberOfAdmin(Records: list):
    num = 0
    for x in Records:
        if x.type == "Administrative":
            num += 1
    return num


# ----------------------------------------------------------------------------------------------

def salaryStatistics(Records: list, n: int):
    totalAcademicSalary = 0
    totalAdminSalary = 0

    for x in Records:
        finalSalary = int(x.basicSalary) + 15 * int(x.numberOfChild)
        if x.materialStatus.lower() == "maried" or x.materialStatus.lower() == "married":
            finalSalary += 20

        if (x.materialStatus.lower() == "maried" or x.materialStatus.lower() == "married") and x.healthInsurance:
            finalSalary -= 12 * (2 + int(x.numberOfChild))

        if x.type == "Administrative":
            totalAdminSalary += finalSalary
        elif x.type == "Academic":
            totalAcademicSalary += finalSalary
        else:
            print("we have an error in line 317")
        if finalSalary > n:
            print(x.name + " with final Salary : " + str(finalSalary))

    print(f"Average academic employees’ salary : {totalAcademicSalary / numberOfAcademiv(Records)}")
    print(f"Average administrative employees’ salary  : {totalAdminSalary / numberOfAdmin(Records)}")


def RetirementInformation(Records: list, n: int):
    for x in Records:
        if not x.status.lower() == "left-university":
            remainFromBirth = 64 - (2022 - int(x.dateOfBith.split('/')[2]))
            remainFromStartingTime = 35 - (2022 - int(x.startingTime.split('/')[1]))
            years = min(remainFromBirth, remainFromStartingTime)
            if years < n:
                print(f"the name : {x.name} and the remaining years = {years}")


def CoursesStatistics(Records: list):
    courses = {}
    academicEmployee = {}
    for x in Records:
        if x.type == "Academic":
            for semester_Year in x.experience:
                for course in x.experience[semester_Year].split(' '):
                    try:
                        courses[course] += 1
                        if x.employeeID not in academicEmployee[course]:
                            academicEmployee[course] = academicEmployee[course] + ' ' + x.employeeID
                    except:
                        courses[course] = 1
                        academicEmployee[course] = x.employeeID

    for course in courses:
        print(
            f"corse = {course} with {courses[course]} times.  with {len(academicEmployee[course].split(' '))} employees ids ={academicEmployee[course]}")
        print("-----------------------------------")


def AdminEmployeesStatistics(Records: list):
    for x in Records:
        vecTotal = 0
        if x.type == "Administrative":
            for year in x.vacation:
                print(f"{x.employeeID} and Year = {year} and vacation days in that year  = {x.vacation[year]}")
                vecTotal += int(x.vacation[year])
            print("-------------------")
            print(f"vacation days = {vecTotal}")
            totalYears = 2022 - int(x.startingTime.split('/')[1])
            print(f"totalYears since starting = {totalYears}")
            print(f"The average number of vacation days per year = {vecTotal} / {totalYears} = {vecTotal / totalYears}")
            print("-------------------")
            print("-------------------")


def AcademicEmployeesStatistics(Records: list):
    list = []
    for x in Records:
        if x.type == "Academic":
            for semester in x.experience:
                for course in x.experience[semester].split(' '):
                    if course not in list:
                        list.append(course)
            print()
            print(
                f"employeeID = {x.employeeID} and Number of semesters = {len(x.experience)} and number of courses ={len(list)}")
            average = len(list) / len(x.experience)
            print(f"average number of courses = {len(list)} / {len(x.experience)} = {average}")
            while list:
                print(list.pop(), end=' ')
            print()
            print("-------------------------------------")


if __name__ == '__main__':
    Records = []
    Records = readGeneral(Records)  # read general data for the Employees
    Records = readAcademic(Records)  # read Academic Employees Data from the file
    Records = readAdmin(Records)  # read Admin Data from the file
    msg = "Welcome to our project \n" \
          "please choose one from the List ...\n" \
          "0) show\n" \
          "1) Add a new employee record\n" \
          "2) Update general attributes\n" \
          "3) Add/update administrative\n" \
          "4) Add/update academic employee attribute\n" \
          "5) Employee's statistics\n" \
          "6) Salary statistics\n" \
          "7) Retirement information\n" \
          "8) Courses statistics\n" \
          "9) Administrative employees statistics\n" \
          "10) Academic employees statistics\n" \
          "15) to break\n"  # Welcome message with list options
    msg2 = "0)to break\n" \
           "1)Employee ID\n" \
           "2)Name\n" \
           "3)Date of birth\n" \
           "4)Marital status\n" \
           "5)Number of Childs\n" \
           "6)Gender\n" \
           "7)Contact information\n" \
           "8)Type\n" \
           "9)Status\n" \
           "10)Department\n" \
           "11)Starting time\n" \
           "12)Basic salary\n" \
           "13)Health insurance\n"  # this for select = 2
    while True:
        select = input(msg)

        if select == "0":
            show(Records)
        if select == "15":
            break
        elif select == "1":

            employeeID = employeeID()

            name1 = name(1)

            name2 = name(2)

            name3 = name(3)

            name = name1 + ' ' + name2 + ' ' + name3

            print("in date Of Bith  it must be    day/month/year...")
            days = input("put here the days  ")
            months = input("put here the month  ")
            year = input("put here the year  ")

            dateOfBith = days + '/' + months + '/' + year

            materialStatus = materialStatus()

            numberOfChilds = numberOfChilds()

            gender = gender()

            print("for Contact information ")
            email = input("put here an email")
            mobile = input("put here a mobile number")
            fax = input("put here a fax number")

            type = type()

            status = status()

            department = input("put here the Department")

            startingTime = input("put here the starting Time")

            basicSalary = basicSalary()

            healthInsurance = healthInsurance()

            if type == "administrative":
                x = Admin(employeeID=employeeID, name=name1 + ' ' + name2 + ' ' + name3, dateOfBith=dateOfBith,
                          materialStatus=materialStatus, numberOfChild=numberOfChilds, gender=gender, email=email,
                          mobile=mobile, fax=fax, type=type, status=status, department=department,
                          startingTime=startingTime, basicSalary=basicSalary, healthInsurance=healthInsurance)
            else:

                x = Academic(employeeID=employeeID, name=name1 + ' ' + name2 + ' ' + name3, dateOfBith=dateOfBith,
                             materialStatus=materialStatus, numberOfChild=numberOfChilds, gender=gender, email=email,
                             mobile=mobile, fax=fax, type=type, status=status, department=department,
                             startingTime=startingTime, basicSalary=basicSalary, healthInsurance=healthInsurance)

            Records.append(x)
        elif select == "2":
          while True:
            while True:
                id = input("give here the employeeID")
                if not isIdExist(Records=Records, id=id):
                    print("you entered a wrong id or ID is not exist please try again")
                else:
                    break
            index = findEmployee(Records, id)
            print("select one from the list to change")
            sel = input(msg2)
            match sel:
                case "0":
                    break
                case "1":
                    Records[index].employeeID = employeeID()

                case "2":
                    name1 = name(i=1)
                    name2 = name(i=2)
                    name3 = name(i=3)

                    Records[index].name = name1 + ' ' + name2 + ' ' + name3

                case "3":
                    print("in date Of Bith  it must be    day/month/year...")
                    days = input("put here the days  ")
                    months = input("put here the month  ")
                    year = input("put here the year  ")
                    Records[index].dateOfBith = days + '/' + months + '/' + year

                case "4":
                    Records[index].materialStatus = materialStatus()

                case "5":
                    Records[index].numberOfChild = numberOfChilds()

                case "6":
                    Records[index].gender = gender()

                case "7":
                    print("for Contact information ")
                    email = input("put here an email")
                    mobile = input("put here a mobile number")
                    fax = input("put here a fax number")
                    Records[index].contantInformation = email + ' ' + mobile + ' ' + fax

                case "8":
                    Records[index].type = type()

                case "9":
                    Records[index].status = status()

                case "10":

                    Records[index].department = input("put here the Department")

                case "11":
                    Records[index].startingTime = input("put here the starting Time")

                case "12":
                    Records[index].basicSalary = str(basicSalary())

                case "13":
                    Records[index].healthInsurance = healthInsurance()
                case default:
                    print("please select from 0 - 13")
        elif select == "3":
            while True:
                id = input("give here the id for Employee to edit")
                if not (isId(id=id) and isIdExist(Records=Records, id=id)):
                    print("you have entered wrong id")
                else:
                    break
            index = findEmployee(Records=Records, id=id)

            if Records[index].type == "Administrative" and not (Records[index].status.lower() == "left-university"):
                year = input("put the year here : ")
                vacationDays = input("number of vacation days : ")
                Records[index].vacation[year] = vacationDays
                print(f"you have changed for {Records[index].employeeID}")
                for i in Records[index].vacation:
                    print(f"year = {i} and vacation days = {Records[index].vacation[i]}")
            else:
                print("this employee is Academic or he left the university ")
        elif select == "4":
            while True:
                id = input("give here the id for Employee to edit")
                if not (isId(id=id) and isIdExist(Records=Records, id=id)):
                    print("you have entered wrong id")
                else:
                    break
            index = findEmployee(Records=Records, id=id)

            if Records[index].type == "Academic" and not (Records[index].status.lower() == "left-university"):
                year = input("put the year here : ")
                semester = input("put the semester here : ")
                courses = input("put the  courses here : ")
                semesterYear = semester + '_' + year
                Records[index].experience[semesterYear] = courses
                print(
                    f"You have changed on Employee with ID = {Records[index].employeeID}  in semester = {semesterYear} with new data = {courses}")
            else:
                print("this employee is Administrative or he left the university ")
        elif select == "5":
            print(f"Number of academic employees = {numberOfAcademiv(Records)}\n"
                  f"Number of administrative employees = {numberOfAdmin(Records)}\n"
                  f"Percent of Full-time employees = {100 * numberOfFullTime(Records) / len(Records)}%\n"
                  f"Number of Male employees = {numOfMale(Records)}\n"
                  f"Number of Female employees = {numOfFemale(Records)}")
        elif select == "6":
            num = input("give here a number ")
            salaryStatistics(Records=Records, n=int(num))
        elif select == "7":
            years = input("put here the Years :  ")
            RetirementInformation(Records=Records, n=int(years))
        elif select == "8":
            CoursesStatistics(Records)
        elif select == "9":
            AdminEmployeesStatistics(Records)
        elif select == "10":
            AcademicEmployeesStatistics(Records)
