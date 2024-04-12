from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import TrialForm

# Create your views here.
    # Home View
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    trial_form = TrialForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'trial_form': trial_form
    })

def add_trial(request, dog_id):
    form = TrialForm(request.POST)
    if form.is_valid():
        new_trial = form.save(commit=False)
        new_trial.dog_id = dog_id
        new_trial.save()
    return redirect('detail', dog_id=dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/{dog_id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'description', 'age', 'titles', 'handler']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'