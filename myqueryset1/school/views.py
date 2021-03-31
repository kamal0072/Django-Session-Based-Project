from django.shortcuts import render
from .models import MyStudentModel

def modelviiw(request):
    # mymodel=MyStudentModel.objects.get(pk=1)

    # mymodel=MyStudentModel.objects.get(name='pappu')
    # mymodel=MyStudentModel.objects.first()
    # mymodel=MyStudentModel.objects.last()
    # mymodel=MyStudentModel.objects.order_by('name').last()
    # mymodel=MyStudentModel.objects.order_by('name').first()
    mymodel=MyStudentModel.objects.order_by('name').first()

    # queries=mymodel.query
    return render(request,'school/modeldata.html',{'model':mymodel})