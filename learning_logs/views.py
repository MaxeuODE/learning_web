from django.shortcuts import render

def index(request):
    '''主页'''
    return render(request,'learning_logs/index.html')