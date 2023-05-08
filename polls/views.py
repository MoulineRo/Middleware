from django.http import HttpResponse
from django.shortcuts import render

from polls.forms import StudentForm


def index(request):
    return HttpResponse("OK")


def new_student(request):
    if request.method == "GET":
        form = StudentForm()
        context = {"form": form}
        return render(request, "new_student.html", context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'new_student.html', {'form': form})
