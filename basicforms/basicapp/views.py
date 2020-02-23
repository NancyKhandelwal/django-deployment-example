from django.shortcuts import render
from basicapp.forms import FormName
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
             print('Validation process successful.')
             print("Name:", form.cleaned_data['Name'])
             print("Email:", form.cleaned_data['Email'])
             print("Text:", form.cleaned_data['Text'])

    return render(request, 'forms.html', {'form': form})
