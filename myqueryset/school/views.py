from django.shortcuts import render
from .models import MyStudentModel

def modelviiw(request):
    # mymodel=MyStudentModel.objects.all()
    # mymodel=MyStudentModel.objects.filter(marks=100)
    # mymodel=MyStudentModel.objects.exclude(marks=100)
    # mymodel=MyStudentModel.objects.order_by('marks')
    # mymodel=MyStudentModel.objects.order_by('-marks')
    # mymodel=MyStudentModel.objects.order_by('?')
    # mymodel=MyStudentModel.objects.order_by('name')
    # mymodel=MyStudentModel.objects.order_by('id')
    # mymodel=MyStudentModel.objects.order_by('id').reverse()
    # mymodel=MyStudentModel.objects.values()
    # mymodel=MyStudentModel.objects.values_list('id','name')
    
    #shows defaul databaes name
    mymodel=MyStudentModel.objects.using('default')
    
    queries=mymodel.query
    return render(request,'school/modeldata.html',{'model':mymodel,'query':queries})