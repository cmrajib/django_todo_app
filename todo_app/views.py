from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    all_items = List.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Item has been added tothe list')


    return render(request,'home.html',{'all_items':all_items})

def about(request):
    return render(request,'about.html',{})

def delete(request, list_id):
    item = List.objects.filter(pk=list_id)
    item.delete()
    messages.success(request,'Item has been delete')
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        # form = ListForm(request.POST or None, instance=item)
        # if form.is_valid():
        item.item = request.POST.get('item')
        item.save()
        messages.success(request,'Item has been edited')
        return redirect('home')
    else:
        return render(request,'edit.html',{'item':item})
