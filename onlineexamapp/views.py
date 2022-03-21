from django.shortcuts import render, redirect
from onlineexamapp.models import Contact, User
from django.http import JsonResponse
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
