import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_old ( request ) :

    html_var = 'f strings'

    html_ = f"""
  

    """

    # return HttpResponse ("Hello, World!")
    return HttpResponse ( html_ )
    # return render( request, "home.html", {} )#Response


def home ( request ) :

    num = random.randint(1,1000000)

    return render ( request, "base.html", { "html_var": True, "num_var": num }  )
