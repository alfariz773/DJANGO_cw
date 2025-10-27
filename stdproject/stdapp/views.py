from django.shortcuts import render

def home(request):
    students = ["james", "jeo", "sam"]
    return render(request, "stdapp/home.html", {'students': students})


def res(request, student_name):
    results = {
        "james": "pass",
        "jeo": "failed",
        "sam": "pass"
    }
    result = results.get(student_name, "not found")
    return render(request, "stdapp/result.html", {"student_name": student_name, "result": result})
