from django.shortcuts import render

def home(request):
    students = ["James", "Jeo", "Sam" , "Alfariz", "Rizky", "Dani", "Buji", "Doraemon", "Nobita", "Suneo", "Giant"]
    return render(request, "stdapp/home.html", {'students': students})


def res(request, student_name):
    results = {
        "James": "PASS",
        "Jeo": "FAILED",
        "Sam": "PASS",
        "Alfariz": "PASS",
        "Rizky": "FAILED",
        "Dani": "PASS",
        "Buji": "FAILED",
        "Doraemon": "PASS",
        "Nobita": "FAILED",
        "Suneo": "PASS",
        "Giant": "FAILED",
        
    }
    result = results.get(student_name, "no result found")
    return render(request, "stdapp/result.html", {"student_name": student_name, "result": result})
