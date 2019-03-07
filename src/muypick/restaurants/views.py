from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home ( request ) :

    html_var = 'f strings'

    html_ = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Page Title</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="main.css">
        <script src="main.js"></script>
    </head>
    <body>

        <h1>Hello, World!</h1>
        <p>This is {html_var} coming through</p>
        
    </body>
    </html>

    """

    # return HttpResponse ("Hello, World!")
    return HttpResponse ( html_ )
    # return render( request, "home.html", {} )#Response

