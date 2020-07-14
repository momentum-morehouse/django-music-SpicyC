from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Album
#from django.contrib.auth.models
#import AbstractUser
# Create your views here.

#added7/15/2020 - to add homepage
# def index(request):
#     all_albums = album.objects.all()
#     return render(request,
#     'albums/list_albums.html', context=
#     {'albums':all_albums}



def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


def add_albums(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})

def album_detail(request, pk):
  album = get_object_or_404(Contact, pk=pk)
  return render(request, "albums/album_detail.html", {"album": album})

# def add_note(request, contact_pk):
#     contact = get_object_or_404(Contact, pk=contact_pk)
#     if request.method == 'GET':
#         form = NoteForm()
#     else:
#         form = NoteForm(data=request.POST)
#         if form.is_valid():
#             new_note = form.save(commit=False)
#             new_note.contact = contact
#             new_note.save()
#             return redirect(to='contact_detail', pk=contact_pk)

    # return render(request, "contacts/add_note.html", {"form": form, "contact": contact})
