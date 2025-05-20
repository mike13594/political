from django.shortcuts import render
from switch_sides_2.forms import OnOffForm

# Create your views here.
def create_3(request):
    onoffform = OnOffForm(request.GET or None)

    context = {
        "onoffform" : onoffform,
    }
    return render(request, 'create.html', context)