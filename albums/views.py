from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from .models import Album
from django.shortcuts import render, redirect, get_object_or_404
from .forms import albumsForm
from django.db import models

# Create your views here.
@login_required
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html',
        {'album': albums})

def add_album(request):
    if request.method == 'GET':
        form = albumsForm()
    else:
        form = albumsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_album.html", {"form": form})

def edit_album(request, pk):
    # album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = albumsForm()
    else:
        form = albumsForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
      "form": form,})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_album.html",
                  {"album": albums})
