from django.shortcuts import render, redirect
from group_14.models.general import Screen
from django import forms

# form class
class AddScreenForm(forms.Form):
    class Meta:
        model = Screen
        fields = ["screen_id", "no_seats"]
    screen_id = forms.IntegerField()
    no_seats = forms.IntegerField()
    
def addScreen(request):
    if request.method == 'POST':
        form = AddScreenForm(request.POST)          #form objects
        if form.is_valid(): 
            # save_screen_obj = Screen.objects.create(screen_id = form.cleaned_data['screen_id'], no_seats = form.cleaned_data['no_seats'])
            # save_screen_obj.save()
            screen = Screen(screen_id=form.cleaned_data['screen_id'], no_seats=form.cleaned_data['no_seats'])
            screen.save()
            return redirect("success!")
        else:
            form = AddScreenForm()
            
    form = AddScreenForm()       
    return render(request=request, template_name="registration/addscreen.html", context={"addScreen_form":form})
        
        
        
    