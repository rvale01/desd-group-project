from django.shortcuts import render, redirect
from group_14.models.general import Screen
from django import forms

class AddScreenForm(forms.Form):
    screen_id = forms.IntegerField()
    no_seats = forms.IntegerField()
    
def addScreen(request):
    if request.method == 'POST':
        form = AddScreenForm(request.POST)
        if form.is_valid():
            screen_model = Screen.objects.create(screen_id = form.cleaned_data['screen_id'], no_seats = form.cleaned_data['no_seats'])
            screen_model.save()
            return redirect("success!")
        else:
            form = AddScreenForm()
            
    return render(request=request, template_name="registration/addscreen.html", context={"addScreen_form":form})
        
        
        
    