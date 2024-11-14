from django.shortcuts import render, redirect
from .forms import RatingForm

def home_page(request):
    return render(request, "index.html")

def submit_rating(request):
    stars = range(1, 6)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('thanks')  
    else:
        form = RatingForm()
        
    return render(request, 'rating.html', {'form': form, 'stars': stars})

def thanks_page(request):
    return render(request, 'thanks.html')
