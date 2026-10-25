from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Student


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll_number = request.POST.get("roll_number")
        email = request.POST.get("email")

        if name and roll_number and email:
            Student.objects.create(
                name=name,
                roll_number=roll_number,
                email=email
            )
            messages.success(request, "Student added successfully!")
            return redirect("home")

    students = Student.objects.all()
    return render(request, "index.html", {"students": students})
def delete_student(request, student_id):
    if request.method == "POST":
        student = get_object_or_404(Student, id=student_id)
        student.delete()
    return redirect("home")
def edit_student(request, student_id):  
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_number = request.POST.get("roll_number")
        student.email = request.POST.get("email")
        student.save()
        return redirect("home")

    return render(request, "edit.html", {"student": student})
