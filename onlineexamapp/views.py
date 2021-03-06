from django.shortcuts import render, redirect
from onlineexamapp.models import Contact, CourseDetail, FacultyCourses, QuestionDetail, TestResult, User
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'index.html')


def support(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message']
        )
        recentContacts = Contact.objects.all().order_by('-id')[:3]
        msg = 'Message Send Successfully !!!'
        return render(request, 'contact.html', {'msg': msg, 'recentContacts': recentContacts})
    else:
        recentContacts = Contact.objects.all().order_by('-id')[:3]
        return render(request, 'contact.html', {'recentContacts': recentContacts})

def emailValidation(request):
    email = request.GET.get('email')
    data = {
        'emailIsTaken': User.objects.filter(email__iexact = email).exists()
    }
    return JsonResponse(data)

def studentSignup(request):
    if request.method == "POST":
        user = User()
        user.userType = request.POST['userType']
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        user.course = request.POST['course']
        user.gender = request.POST['gender']
        user.address = request.POST['address']
        user.profilePic = request.FILES['profilePic']
        # user.save()
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email Already Registered'
            return render(request, 'studentSignup.html', {'msg': msg, 'user': user})
        except:
            if request.POST['course'] == "Selecy Your Course":
                msg = 'Please Select Your Course'
                return render(request, 'studentSignup.html', {'msg': msg, 'user': user})
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    userType=request.POST['userType'],
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    course=request.POST['course'],
                    gender=request.POST['gender'],
                    password=request.POST['password'],
                    address=request.POST['address'],
                    profilePic=request.FILES['profilePic'],
                )
                fullName = request.POST['fname'] + ' ' + request.POST['lname']
                msg = 'Your Account Created Successfully'
                return render(request, 'login.html', {'msg': msg, 'fullName': fullName})
            else:
                msg = 'Password Mismatch'
                return render(request, 'studentSignup.html', {'msg': msg, 'user': user})
    else:
        return render(request, 'studentSignup.html')


def login(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST['email']
        try:
            userData = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == userData.password:
                if userData.userStatus == "Pending":
                    msg = 'You Are Not Approved By Higher Authority'
                    return render(request, 'login.html', {'msg': msg})
                else:
                    request.session['email'] = userData.email
                    request.session['fname'] = userData.fname
                    request.session['profilePic'] = userData.profilePic.url
                    request.session['userType'] = userData.userType
                    msg = 'Login Successfully'
                    return render(request, 'index.html', {'msg': msg})
            else:
                msg = 'Incorrect Password'
                return render(request, 'login.html', {'msg': msg, 'user': user})
        except:
            msg = 'Email Not Registered'
            return render(request, 'studentSignup.html', {'msg': msg})
    else:
        return render(request, 'login.html')


def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profilePic']
        del request.session['userType']
        return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def facultySignup(request):
    if request.method == "POST":
        user = User()
        user.userType = request.POST['userType']
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        user.gender = request.POST['gender']
        user.address = request.POST['address']
        # user.save()
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email Already Registered'
            return render(request, 'facultySignup.html', {'msg': msg, 'user': user})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    userType=request.POST['userType'],
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    gender=request.POST['gender'],
                    password=request.POST['password'],
                    address=request.POST['address'],
                )
                fullName = request.POST['fname'] + ' ' + request.POST['lname']
                msg = 'Your Account Created Successfully'
                return render(request, 'login.html', {'msg': msg, 'fullName': fullName})
            else:
                msg = 'Password Mismatch'
                return render(request, 'facultySignup.html', {'msg': msg, 'user': user})
    else:
        return render(request, 'facultySignup.html')

def changePassword(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.session['email'])
        if user.password == request.POST['oldPassword']:
            if request.POST['newPassword'] == request.POST['newcPassword']:
                if request.POST['oldPassword'] != request.POST['newPassword']:
                    user.password = request.POST['newPassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = 'Old and New Password Can\'t Be  Same'
                    return render(request, 'changePassword.html', {'msg': msg})
            else:
                msg = 'New Password Does Not Match'
                return render(request, 'changePassword.html', {'msg': msg})
        else:
            msg = 'Invalid Password'
            return render(request, 'changePassword.html', {'msg': msg})
    else:
        return render(request, 'changePassword.html')

def studentList(request):
    studentsList = User.objects.filter(userType = "Student")
    return render(request, 'studentList.html', {'studentsList': studentsList})

def studentApprove(request):
    userId = request.GET.get('id', None)
    user = User.objects.get(id = userId)
    if user.userStatus == "Approved":
        user.userStatus = "Pending"
    else:
        user.userStatus = "Approved"
    user.save()
    data = { 'status' : 'Status Updated' }
    return JsonResponse(data)

def addCourse(request):
    if request.method == "POST":
        facultyDetail = User.objects.get(email = request.session['email'])
        CourseDetail.objects.create(
            facultyDetail = facultyDetail,
            courseName = request.POST['courseName']
        )
        msg = "Course Added Successfully"
        courseDetail = CourseDetail.objects.all()
        return render(request, 'addCourse.html', { 'msg': msg, 'courseDetail': courseDetail })
    else:
        courseDetail = CourseDetail.objects.all()
        return render(request, 'addCourse.html', { 'courseDetail': courseDetail })

def addQuestion(request):
    courseDetail = CourseDetail.objects.all()
    if request.method == "POST":
        addquestion = QuestionDetail()
        # addquestion.courseName = request.POST['courseName']
        addquestion.question = request.POST['question']
        addquestion.option1 = request.POST['option1']
        addquestion.option2 = request.POST['option2']
        addquestion.option3 = request.POST['option3']
        addquestion.option4 = request.POST['option4']
        # addquestion.answer = request.POST['answer']
        if request.POST['courseName'] == "Select Course" or request.POST['answer'] == "Select Correct Option":
            msg = "Select Field Is Required"
            return render(request, 'addQuestion.html', { 'courseDetail': courseDetail, 'msg': msg, 'addquestion': addquestion })
        else:
            courseName = CourseDetail.objects.get(id = request.POST['courseName'])
            QuestionDetail.objects.create(
                courseName = courseName,
                question = request.POST['question'],
                option1 = request.POST['option1'],
                option2 = request.POST['option2'],
                option3 = request.POST['option3'],
                option4 = request.POST['option4'],
                answer = request.POST['answer']
            )
            msg = "Question Added Successfully"
            return render(request, 'addQuestion.html', { 'courseDetail': courseDetail, 'msg': msg })
    else: 
        return render(request, 'addQuestion.html', { 'courseDetail': courseDetail })

def studentTest(request):
    courseDetail = CourseDetail.objects.all()
    return render(request, 'studentTest.html', { 'courseDetail': courseDetail })

def studentTestInfo(request, courseName):
    return render(request, 'studentTestInfo.html', { 'courseName': courseName })

def startTest(request, courseName):
    courseDetail = CourseDetail.objects.get(courseName = courseName)
    questionDetail = QuestionDetail.objects.filter(courseName = courseDetail)
    return render(request, 'testPage.html', { 'questionDetail': questionDetail, 'courseName': courseDetail.courseName })

def submitTest(request):
    user = User.objects.get(email = request.session['email'])
    l = list(request.POST.items())
    # print(len(l))
    # print(l[1:len(l)-1])
    answerSheet = l[1:len(l)-1]
    # print(answerSheet)
    
    marks = 0
    if answerSheet:
        for i in answerSheet:
            question = QuestionDetail.objects.get(id = i[0])
            course = CourseDetail.objects.get(courseName = question.courseName.courseName)
            # print(question.courseName.courseName)
            # print("Answer of " + str(question.id) + " = " + question.answer)
            # print("Student Select = " + i[1])
            if question.answer == i[1]:
                # print(question.answer)
                marks += 1
        # print(marks)

        TestResult.objects.create(
            student = user,
            course = course,
            testCourse = question.courseName.courseName,
            marks = marks
        )

        subject = '[INFITA] Exam Result'
        message = 'Hello ' + user.fname + ', Your gave exam for ' + question.courseName.courseName + ' subject.\nIn which you obtain : ' + str(marks) + ' marks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return redirect('studentTestResult')
    else:
        return redirect('studentTest')

def studentTestResult(request):
    student = User.objects.get(email= request.session['email'])
    result = TestResult.objects.filter(student = student)
    return render(request, 'studentResult.html', { 'result': result })

def facultyCourseResult(request):
    tempList = []
    studentList = []
    faculty = User.objects.get(email = request.session['email'])
    facultyCourse = FacultyCourses.objects.filter(faculty = faculty)
    # print(list(facultyCourse))
    for i in range(len(facultyCourse)):
        result = TestResult.objects.filter(testCourse = facultyCourse[i].facultyCourse)
        for j in range(len(result)):
            # print(result[j].marks)
            tempList.append(result[j].student.fname)
            tempList.append(result[j].student.lname)
            tempList.append(result[j].student.course)
            tempList.append(result[j].testCourse)
            tempList.append(result[j].marks)
            tempList.append(result[j].date)
            studentList.append(tempList)
            print(studentList)
            tempList = []
            # print(studentList)

        # fc['marks'] = result.id
    print()
    print(studentList)
    # print(result)
    # print(len(result))

    # course = CourseDetail.objects.get(facultyDetail = faculty)
    # result = TestResult.objects.filter(course = course)
    
    result = TestResult.objects.all()
    return render(request, 'facultyCourseResult.html', { 'studentList': studentList })

def facultyCourse(request):
    faculty = User.objects.get(email = request.session['email'])
    facultyCourseList = FacultyCourses.objects.filter(faculty = faculty)
    if request.method == "POST":
        if request.POST['facultycourse'] == "--- Select Your Skill ---":
            msg = "Please Select Your Course"
            return render(request, 'facultyCourse.html', { 'facultyCourseList': facultyCourseList, 'msg': msg })
        else:
            try:
                FacultyCourses.objects.get(faculty = faculty, facultyCourse = request.POST['facultycourse'])
                msg = "This Course Is Already Selected"
                return render(request, 'facultyCourse.html', { 'facultyCourseList': facultyCourseList, 'msg': msg })
            except:
                FacultyCourses.objects.create(
                    faculty = faculty,
                    facultyCourse = request.POST['facultycourse']
                )
                return render(request, 'facultyCourse.html', { 'facultyCourseList': facultyCourseList })
    else:
        return render(request, 'facultyCourse.html', { 'facultyCourseList': facultyCourseList })
