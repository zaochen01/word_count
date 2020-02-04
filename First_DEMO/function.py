from django.http import  HttpRequest, HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'hello123.html')

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    word_count = {}
    for word in user_text:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    print(total_count)
    return render(request,'login/hello.html',
                  {'count':total_count,'worddict':word_count})