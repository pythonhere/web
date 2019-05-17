from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Appointment, Contact
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'hospital/index.html')


def about(request):
    return render(request, 'hospital/about.html')


def appointment(request):
    return render(request, 'hospital/appointment.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contactus = Contact(name=name , email=email , subject=subject , message=message )
        contactus.save()

    return render(request, 'hospital/contact.html',{"data1":"data1"})



def doctorprofile(request):
    return render(request, 'hospital/doctorprofile.html')


def single(request):
    return render(request, 'hospital/single.html')

def doctor1(request):
    return render(request, 'hospital/doctor1.html')

def doctor2(request):
    return render(request, 'hospital/doctor2.html')

def doctor3(request):
    return render(request, 'hospital/doctor3.html')

def doctor4(request):
    return render(request, 'hospital/doctor4.html')

def doctor5(request):
    return render(request, 'hospital/doctor5.html')

def doctor6(request):
    return render(request, 'hospital/doctor6.html')

def doctor7(request):
    return render(request, 'hospital/doctor7.html')

def doctor8(request):
    return render(request, 'hospital/doctor8.html')

def doctor9(request):
    return render(request, 'hospital/doctor9.html')

def doctor10(request):
    return render(request, 'hospital/doctor10.html')

def doctor11(request):
    return render(request, 'hospital/doctor11.html')

def doctor12(request):
    return render(request, 'hospital/doctor12.html')

def doctor13(request):
    return render(request, 'hospital/doctor13.html')

def doctor14(request):
    return render(request, 'hospital/doctor14.html')

def gallery(request):
    return render(request, 'hospital/gallery.html')


def staffprofile(request):
    return render(request, 'hospital/staffprofile.html')

def profile(request):
    return render(request, 'hospital/profile.html')

def pateintform(request):
    return render(request, 'hospital/patientform.html')

def auth(request):
    return render(request, 'hospital/auth.html')

def authL(request):
    return render(request, 'hospital/authL.html')

def authR(request):
    return render(request, 'hospital/authR.html')

def thankyou(request):
    return render(request, 'hospital/thankyou.html')



def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username" ,"")
        email= request.POST.get("email" ,"")
        password = request.POST.get("password" ,"")
        if  User.objects.filter(username=username).exists() is not True \
                or User.objects.filter(email=email).exists() is not True:
            User.objects.create_user(username,email,password)
            return HttpResponseRedirect(reverse('hospital:index'))
        else:
            msg = {'msg' : "user already exists"}
        return render(request, 'hospital/authR.html', msg)

    else:
        return render(request,'hospital/index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username' , '')
        password = request.POST.get('password' , "")
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
              login(request,user)
              return HttpResponseRedirect(reverse('hospital:index'))

        else:
            msg = {'msg' : "wrong email or password"}
            return  render(request, 'hospital/authL.html', msg)
        return  HttpResponseRedirect(reverse('hospital:index'))
    else:
        return render(request,'hospital/index.html')

def user_welcome(request):
    return render(request,'hospital/index.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hospital:index'))

def patientform(request):
    if request.method == "POST":
        address = request.POST.get('address' , '')
        mobile = request.POST.get('mobile' , '')
        image = request.FILES.get('image','')
        fileno = request.POST.get('fileno','')
        dob = request.POST.get('dob','')
        age = request.POST.get('age','')
        issue = request.POST.get('issue','')
        pastissue = request.POST.get('pastissue','')

        prescription = request.POST.get('prescription','')
        bill = request.FILES.get('bill','')
        user = request.user
        profile = Profile(user=user , address=address , mobile=mobile , image=image ,fileno=fileno, dob=dob , age=age ,issue=issue ,prescription=prescription  ,pastissue=pastissue ,  bill=bill)
        profile.save()
        userProfile = Profile.objects.get(user=user)
        return render(request, 'hospital/patientform.html' , {'profile' :userProfile})

    else:
        try:
            user =  request.user
            userProfile = Profile.objects.get(user=user)
            return render(request, 'hospital/patientform.html', {'profile': userProfile})
        except:
            return render(request , 'hospital/patientform.html')

def update_patient_profile(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user=user)
        address = request.POST.get('address', '')
        mobile = request.POST.get('mobile', '')
        image = request.FILES.get('image', '')
        fileno = request.POST.get('fileno','')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age','')
        issue = request.POST.get('issue', '')
        pastissue = request.POST.get('pastissue', '')
        prescription = request.POST.get('prescription', '')
        bill = request.FILES.get('bill', '')
        profile.address = address
        profile.mobile = mobile
        profile.image = image
        profile.fileno=fileno
        profile.age=age
        profile.dob=dob
        profile.issue=issue
        profile.prescription=prescription
        profile.pastissue=pastissue
        profile.bill=bill
        print(profile)
        profile.save()

        userProfile = Profile.objects.get(user=user)
        return render(request, 'hospital/patientform.html', {'profile': userProfile})
    else:
        return HttpResponseRedirect(reverse('hospital:index'))


# def staffform(request):
#     if request.method=='POST':
#         address = request.POST.get('address', '')
#         image = request.FILES.get('image', '')
#         sid = request.POST.get('sid', '')
#         dob = request.POST.get('dob', '')
#         age = request.POST.get('age', '')
#         designation = request.POST.get('designation', '')
#         department = request.POST.get('department', '')
#         number = request.POST.get('number', '')
#         qualification = request.POST.get('qualification', '')
#
#         user = request.user
#         staff = StaffProfile(user=user, address=address, image=image, sid=sid, dob=dob, age=age,
#                           designation=designation , department=department, qualification=qualification, number=number)
#         staff.save()
#         staffNewProfile = StaffProfile.objects.get(user=user)
#         return render(request, 'hospital/staffform.html', {'profile': staffNewProfile})
#
#     else:
#         try:
#             user = request.user
#             print(user)
#             staff = StaffProfile.objects.get(user=user)
#             print("---",staff.sid)
#             msg = {"profileStaff":staff}
#             print(msg)
#             return render(request , 'hospital/staffform.html' ,msg)
#         except Exception as e:
#             print(e)
#             return render(request, 'hospital/staffform.html')
#
#
# def update_staff_profile(request):
#     if request.method == "POST":
#         user = request.user
#         staff = StaffProfile.objects.get(user=user)
#         address = request.POST.get('address', '')
#
#         image = request.FILES.get('image', '')
#         sid = request.POST.get('sid', '')
#         dob = request.POST.get('dob', '')
#         age = request.POST.get('age', '')
#         designation = request.POST.get('designation', '')
#         department = request.POST.get('department', '')
#         number = request.POST.get('number', '')
#         qualification = request.POST.get('qualification', '')
#         staff.address = address
#
#         staff.image = image
#         staff.sid = sid
#         staff.age = age
#         staff.dob = dob
#         staff.designation = designation
#         staff.department = department
#         staff.number = number
#         staff.qualification = qualification
#
#         print(staff)
#         staff.save()
#
#         staff = StaffProfile.objects.get(user=user)
#         return render(request, 'hospital/staffform.html', {'staffprofile': staff})
#     else:
#         return HttpResponseRedirect(reverse('hospital:index'))
#
# def doctorform(request):
#     if request.method=='POST':
#         address = request.POST.get('address', '')
#         image = request.FILES.get('image', '')
#
#         dob = request.POST.get('dob', '')
#         age = request.POST.get('age', '')
#         designation = request.POST.get('designation', '')
#         department = request.POST.get('department', '')
#         number = request.POST.get('number', '')
#         qualification1 = request.POST.get('qualification1', '')
#         qualification2 = request.POST.get('qualification2', '')
#         qualification3 = request.POST.get('qualification3', '')
#         qualification4 = request.POST.get('qualification4', '')
#         experience1 = request.POST.get('experience1', '')
#         experience2 = request.POST.get('experience2', '')
#         experience3 = request.POST.get('experience3', '')
#         experience4 = request.POST.get('experience4', '')
#         experience5 = request.POST.get('experience5', '')
#         user = request.user
#         doctor = DoctorProfile(user=user, address=address, image=image,  dob=dob, age=age,designation=designation , experience1=experience1 , experience2=experience2 , experience3=experience3 , experience4=experience4 , experience5=experience5  , department=department, qualification1=qualification1 , qualification2=qualification2 , qualification3=qualification3 , qualification4=qualification4 , number=number)
#         doctor.save()
#         doctorNewProfile = DoctorProfile.objects.get(user=user)
#         return render(request, 'hospital/doctorform.html', {'profile': doctorNewProfile})
#
#     else:
#         try:
#             user = request.user
#
#             doctor = DoctorProfile.objects.get(user=user)
#
#             msg = {"profiledoctor":doctor}
#
#             return render(request , 'hospital/doctorform.html' ,msg)
#         except Exception as e:
#             print(e)
#             return render(request, 'hospital/doctorform.html')
#
#
# def update_doctor_profile(request):
#     if request.method == "POST":
#         user = request.user
#         doctor = DoctorProfile.objects.get(user=user)
#         address = request.POST.get('address', '')
#
#         image = request.FILES.get('image', '')
#         experience = request.POST.get('sid', '')
#         dob = request.POST.get('dob', '')
#         age = request.POST.get('age', '')
#         designation = request.POST.get('designation', '')
#         department = request.POST.get('department', '')
#         number = request.POST.get('number', '')
#         qualification = request.POST.get('qualification', '')
#         doctor.address = address
#
#         doctor.image = image
#         doctor.experience = experience
#         doctor.age = age
#         doctor.dob = dob
#         doctor.designation = designation
#         doctor.department = department
#         doctor.number = number
#         doctor.qualification = qualification
#
#         print(doctor)
#         doctor.save()
#
#         doctor = DoctorProfile.objects.get(user=user)
#         return render(request, 'hospital/doctorform.html', {'doctorprofile': doctor})
#     else:
#         return HttpResponseRedirect(reverse('hospital:index'))


def appointment(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        doa = request.POST.get('doa', '')
        fileno = request.POST.get('fileno', '')
        number = request.POST.get('number', '')
        cdoctor = request.POST.get('cdoctor', '')
        timetable = request.POST.get('timetable', '')
        appoint = Appointment(user=user, fileno=fileno, name=name, email=email, cdoctor=cdoctor ,  doa=doa,  timetable=timetable, number=number)
        appoint.save()
        appontment=Appointment.objects.get(user=user)
        return render(request, 'hospital/thankyou.html', {'appointments': appontment})
    else:
        try:
            user = request.user

            appoint = appointment.objects.get(user=user)

            msg = {"profileappoint":appoint}

            return render(request, 'hospital/thankyou.html', msg)
        except Exception as e:
            print(e)
            return render(request, 'hospital/appointment.html')

def patientlist(request):
     # doctor
     # appointment -> patient

     doc_user = request.user
     doc_name = doc_user.username
     data = Appointment.objects.filter(cdoctor=doc_name);
     return render(request , 'hospital/patientlist.html' , {'data':data });


def patientd(request):
    pid = request.GET.get('pid','')
    p_profile = Profile.objects.get(id = pid)
    return render(request,'hospital/patientd.html' , {'profile':p_profile})

def docprofile(request):
    doc_name = request.GET.get('doc','')
    user = User.objects.get(username=doc_name);
    doc_profile = DoctorProfile.objects.get(user_id=user.id)
    return  render(request,'hospital/docprofile.html', {'dprofile' : doc_profile});