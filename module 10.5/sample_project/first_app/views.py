from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    context = {
        "fruits": ["Apple", "Banana", "Strawberry", "Orange"],
        "name": "my mother's name is Rita",
        "my_name": "Sujay",
        "birthday": datetime.datetime.now(),
        "empty_string": "",
        "mycar": {
            "brand": "Ford",
            "model": "Mustang",
            "year": "1964",
        },
        "employee": [
            {"name": "zed", "age": 20},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 19},
        ],
        "number": 21,
        "file_size": 123456789,
        "post": "my FIRST post",
        "animals": "cat\ndog\nhouse",
        "mybirthdate": datetime.datetime(2000, 7, 20),
        "mydate": datetime.datetime(2023, 12, 30),
        "mybirthdate": datetime.datetime(2000, 7, 20),
        "date1": datetime.datetime(2022, 6, 8, 9, 30),
        "date2": datetime.datetime(2022, 6, 8, 13, 45),
    }

    return render(request, "first_app/index.html", context)
