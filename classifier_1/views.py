from django.shortcuts import render
from classifier_1.models import ClassifierModel

# Create your views here.
def classifier_1(request):


    # context = {
    #             "classify" : classify,                
    #         }
    return render(request, 'classifier.html')