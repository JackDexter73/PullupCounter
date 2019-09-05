from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Exercises
from .forms import ExerciseForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class BootstrapTestView(TemplateView):
    template_name = 'testbootstrap.html'

# Create your views here.
def initialtest(request):
    return HttpResponse("this is a test!")

def secondtest(request):
    return HttpResponse('<h1>This is a second test</h1>')



def fifthtest(request):
    form = ExerciseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ExerciseForm

    context ={
        "form": form,
    }
    return render(request, 'formtest.html', context)






def thirdtest(request):
    history = Exercises.objects.all()
    total = 0
    for item in history:
        total += int(item.reps)
    #print('total is equal to', total)
    numberofreps = request.POST.get("reps")
    my_context ={
        "first": numberofreps,
        "second": total,
        "third": history,
    }
    #print(numberofreps)
    #exercisetype = request.POST.get("typeofexercise")

    #exercisetype = request.POST.get("typeofexercise")
    #print(exercisetype)
    #reps = request.Post.get("reps")
    #newSet = Exercises(exercise= exercisetype, reps=reps)
    #newSet.save()
    return render(request, 'home.html', my_context)

#def displayreps(request):
#    history = Exercises.objects.all()
#    pullupTotal = 0
#    pushupTotal = 0
#    rowTotal = 0
#    repsleft = 0
#    for item in history:
#        if item.exercise == "pullup":
#            pullupTotal += int(item.reps)
#        elif item.exercise == "pushup":
#            pushupTotal += int(item.reps)
#        elif item.exercise == "row":
#            rowTotal += int(item.reps)
#        else:
#            repsleft += int(item.reps)
#    my_context ={
#        "pullups": pullupTotal,
#        "pushups": pushupTotal,
#        "rows": rowTotal,
#        "repsleft": repsleft,
#    }
#    return render(request, 'home.html', my_context)

def addrepstodatabase(request):
    exercisetype = request.POST.get("typeofexercise")
    reps = request.POST.get("reps")
    print("whatever")
    if reps != "": 
        newSet = Exercises(exercise= exercisetype, reps=reps)
        newSet.save()
    else:
        print("Try again you typed " + str(reps) +" this is not a number")
  
    if exercisetype == "pushup":
        return HttpResponseRedirect('/pushups/')
    elif exercisetype == "pullup":
        return HttpResponseRedirect('/pullups/')
    elif exercisetype == "row":
        return HttpResponseRedirect('/rows/')
    elif exercisetype == "squat":
        return HttpResponseRedirect('/squats/')
    else:
        return HttpResponseRedirect('/home/')

def homeView(request):
    history = Exercises.objects.all()
    pullupTotal = 0
    pushupTotal = 0
    rowTotal = 0
    squatTotal = 0
    repsleft = 0
    for item in history:
        if item.exercise == "pullup":
            pullupTotal += int(item.reps)
        elif item.exercise == "pushup":
            pushupTotal += int(item.reps)
        elif item.exercise == "row":
            rowTotal += int(item.reps)
        elif item.exercise == "squat":
            squatTotal += int(item.reps)
        else:
            repsleft += int(item.reps)
    my_context ={
        "pullups": pullupTotal,
        "pushups": pushupTotal,
        "rows": rowTotal,
        "squats": squatTotal,
        "repsleft": repsleft,
    }
    return render(request, 'home.html', my_context)

def pullupsView(request):
    history = Exercises.objects.all()
    pullupTotal = 0
    pushupTotal = 0
    rowTotal = 0
    squatTotal = 0
    repsleft = 0
    for item in history:
        if item.exercise == "pullup":
            pullupTotal += int(item.reps)
        elif item.exercise == "pushup":
            pushupTotal += int(item.reps)
        elif item.exercise == "row":
            rowTotal += int(item.reps)
        elif item.exercise == "squat":
            squatTotal += int(item.reps)
        else:
            repsleft += int(item.reps)
    my_context ={
        "pullups": pullupTotal,
        "pushups": pushupTotal,
        "rows": rowTotal,
        "repsleft": repsleft,
    }
    return render(request, 'pullups.html', my_context)

def pushupsView(request):
    history = Exercises.objects.all()
    pullupTotal = 0
    pushupTotal = 0
    rowTotal = 0
    squatTotal = 0
    repsleft = 0
    for item in history:
        if item.exercise == "pullup":
            pullupTotal += int(item.reps)
        elif item.exercise == "pushup":
            pushupTotal += int(item.reps)
        elif item.exercise == "row":
            rowTotal += int(item.reps)
        elif item.exercise == "squat":
            squatTotal += int(item.reps)
        else:
            repsleft += int(item.reps)
    my_context ={
        "pullups": pullupTotal,
        "pushups": pushupTotal,
        "rows": rowTotal,
        "squats": squatTotal,
        "repsleft": repsleft,
    }
    return render(request, 'pushups.html', my_context)    

def rowsView(request):
    history = Exercises.objects.all()
    pullupTotal = 0
    pushupTotal = 0
    rowTotal = 0
    squatTotal = 0
    repsleft = 0
    for item in history:
        if item.exercise == "pullup":
            pullupTotal += int(item.reps)
        elif item.exercise == "pushup":
            pushupTotal += int(item.reps)
        elif item.exercise == "row":
            rowTotal += int(item.reps)
        elif item.exercise == "squat":
            squatTotal += int(item.reps)
        else:
            repsleft += int(item.reps)
    my_context ={
        "pullups": pullupTotal,
        "pushups": pushupTotal,
        "rows": rowTotal,
        "squats": squatTotal,
        "repsleft": repsleft,
    }
    return render(request, 'rows.html', my_context)

def squatsView(request):
    history = Exercises.objects.all()
    pullupTotal = 0
    pushupTotal = 0
    rowTotal = 0
    squatTotal = 0
    repsleft = 0
    for item in history:
        if item.exercise == "pullup":
            pullupTotal += int(item.reps)
        elif item.exercise == "pushup":
            pushupTotal += int(item.reps)
        elif item.exercise == "row":
            rowTotal += int(item.reps)
        elif item.exercise == "squat":
            squatTotal += int(item.reps)
        else:
            repsleft += int(item.reps)
    my_context ={
        "pullups": pullupTotal,
        "pushups": pushupTotal,
        "rows": rowTotal,
        "squats": squatTotal,
        "repsleft": repsleft,
    }
    return render(request, 'squats.html', my_context)



#def educationview(request):
#    ListOfProjects = Exercises.objects.all()
#    my_context ={
#        "first": ListOfProjects,
#    }
#
#    title = request.POST.get("title")
#    difficulty = request.POST.get("projectdiff")
#    description = request.POST.get("projectdescription")
#    newProject = Project(title = title, difficulty = difficulty, description = description)
#    newProject.save()
#
#    return render(request, "education.html", my_context)
