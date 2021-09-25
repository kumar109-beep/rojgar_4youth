from django.shortcuts import render
import logging

def home(request):
    a = {'dept': 'sales', 'code': 6734, 'name': 'john'}
    logging.error(a)
    return render(request,'index.html')

