from django.shortcuts import render

def regirter(request):
        return render(request, 'users/registration.html')
