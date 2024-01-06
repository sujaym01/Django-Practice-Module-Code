from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # print(form)
            print(form.cleaned_data)
        else:
            return render(request, './first_app/home.html', {'form': form})
    else:
        form = ExampleForm()
    return render(request, './first_app/home.html', {'form': form })


from first_app.forms import StudentForm

def index(request):
    student = StudentForm()
    return render(request, './first_app/index.html', {'form': student})