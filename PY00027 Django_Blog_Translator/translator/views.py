import translator
from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request):
    if request.method == 'POST': 
        original_text = request.POST['my_textarea']#to get test entered in the box
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text}) #after getting text to display in second box
    else:
        return render(request, 'translator.html')#if text not entered only translator.html will requested