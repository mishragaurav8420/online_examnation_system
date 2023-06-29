from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from ots.models import *

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
def candidateRegistrationForm(request):
    pass
def candidateRegistration(request):
    pass
def loginView(request):
    pass
def candidateHome(request):
    pass
def testPaper(request):
    pass
def calculateTestResult(request):
    pass
def testResultHistory(request):
    pass
def showTestResult(request):
    pass
def logoutView(request):
    pass

# Create your views here.
