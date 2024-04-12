from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Event
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
    id_list = dog.events.all().values_list('id')
    events_dog_no_participation = Event.objects.exclude(id__in=id_list)
    trial_form = TrialForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'trial_form': trial_form,
        'events': events_dog_no_participation,
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
    fields = ['name', 'breed', 'description', 'titles', 'handler', 'microchipnr', 'age']
    success_url = '/dogs/{dog_id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'description', 'age', 'titles', 'handler']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'

class EventList(ListView):
  model = Event

class EventDetail(DetailView):
  model = Event

class EventCreate(CreateView):
  model = Event
  fields = '__all__'

class EventUpdate(UpdateView):
  model = EventCreate
  fields = ['name', 'date']

class EventDelete(DeleteView):
  model = Event
  success_url = '/events'

def assoc_event(request, dog_id, event_id):
  Dog.objects.get(id=dog_id).events.add(event_id)
  return redirect('detail', dog_id=dog_id)

def unassoc_event(request, dog_id, event_id):
  Dog.objects.get(id=dog_id).events.remove(event_id)
  return redirect('detail', dog_id=dog_id)