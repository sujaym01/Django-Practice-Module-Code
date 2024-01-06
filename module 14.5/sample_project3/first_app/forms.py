from django import forms
from django.forms.widgets import NumberInput
import datetime
# Create your forms here.

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class ExampleForm(forms.Form):
    # CharField() : collecting one line  text inputs such as name or address.
    name = forms.CharField()

    # CharField() with Textarea widget : collecting multi-line text inputs such as comment or message field.
    #  the default number of rows is 10
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    # EmailField()
    email = forms.EmailField()

    # BooleanField()
    # The default is False and renders an unclicked checkbox in the HTML template
    cheek = forms.BooleanField()

    # DateField() only accepts date formatted values such as 2020-07-30. 
    date = forms.DateField()

    # DateField() with NumberInput widget attribute
    # looking to add a calendar, import NumberInput at the top of the file
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # looking to add a calendar wirh local time
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    # DateField() with SelectDateWidget widget
    # the build-in SelectDateWidget which displays three drop-down menus for month, date, and year.
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()

    # required (Boolean)
    # The argument is assigned to every field and is True by default.
    email_address = forms.EmailField( 
    required = False,
    )

    # max_length and min_length
    message = forms.CharField(
	max_length = 10,
    )

    # label (String) 
    email_address = forms.EmailField( 
    label="Please enter your email address",
    )

    # initial (String) for CharField()
    first_name = forms.CharField(initial='Your name')

    # initial (Boolean) for BooleanField()
    agree = forms.BooleanField(initial=True)

    # initial (Datetime) for DateField()
    # Import datetime at the top of the file
    day = forms.DateField(initial=datetime.date.today)



    # ChoiceField, MultipleChoiceField

    # ChoiceField()
    CHOICES = [
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ]
    # Use the Django ChoiceField to create a drop-down menu of choices.
    # favorite_color = forms.ChoiceField(choices=CHOICES)

    # ChoiceField() with RadioSelect widget
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


    # MultipleChoiceField()
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    # favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # add the widget CheckboxSelectMutiple to have the choices render next to checkboxes.
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)



from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'roll': 'Student Roll'
        }