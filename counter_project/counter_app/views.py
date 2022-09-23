from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'user' not in request.session:
        request.session['user'] = 0
    else:
        request.session['user'] += 0
    return render(request, "index.html")


def add_input(request):
    try:
        user_input = int(request.POST["user"])
        request.session["user"] += user_input
    except:
        print("This is not working")
    return redirect('/')


def two(request):
    if 'user' not in request.session:
        request.session['user'] = 0
    else:
        request.session['user'] += 2
    return redirect('/')



def destroy(request):
    if 'user' in request.session:
        del request.session['user']
    else:
        print("key 'user' does not exit")
    return redirect('/')


