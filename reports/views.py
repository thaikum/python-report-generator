from django.shortcuts import render

from reports.models import Student
from reports.report_generator import Report


def homepage(request):
    students = Student.objects.all()
    pdf_gen = Report()

    pdf_gen.data = students
    pdf_gen.columns = ['first_name', 'middle_name', 'age']
    pdf_gen.display_names = ['First Name', 'Second Name', 'Age']
    pdf_gen.title = 'A report of all the students in the database'
    pdf_gen.logo_directory = '/reports/static/reports/images/image.png'
    pdf_gen.address = "SP Geolocator\nNairobi\nCounty"
    pdf = pdf_gen.pdf_generator()
    return render(request, 'reports/index.html', context={'pdf': pdf})
