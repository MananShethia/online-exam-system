from django.shortcuts import render
from onlineexamapp.models import User

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
    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        user = User()
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        user.gender = request.POST['gender']
        user.address = request.POST['address']
        # user.save()
        try:
            User.objects.get(email = request.POST['email'])
            msg = 'Email Already Registered'
            return render(request, 'signup.html', {'msg': msg, 'user': user})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    gender = request.POST['gender'],
                    password = request.POST['password'],
                    address = request.POST['address'],
                )
                fullName = request.POST['fname'] + ' ' + request.POST['lname']
                msg = 'Your Account Created Successfully'
                return render(request, 'login.html', {'msg': msg, 'fullName': fullName})
            else:
                msg = 'Password Mismatch'
                return render(request, 'signup.html', {'msg': msg, 'user': user})
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')