from django.shortcuts import render
def Tana(requset):
    name = "Tana"
    Age = 21
    Blance = 10000000.00
    context = {'name':name, 'Age':Age, 'Balance':Blance }

# Create your views here.

def home(request):
    nameteam = 'Team Frank'
    rank = 1
    company = "DBT 3R1"

    return render(request, '1.html', {
        'nameteam': nameteam,'rank' : rank , 'company' : company
    })