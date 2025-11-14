from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm


def competition_home(request):
    """
    Renders the home page of the competition app,
    displaying the most recent winner.
    """
    winner = Entry.objects.filter(is_winner=True).order_by
    ('-date_submitted').first()
    return render(request, 'competition/home.html', {'winner': winner})


def vote_page(request):
    """
    Renders the voting page, displaying all entries
    """
    entries = Entry.objects.filter(is_winner=False).order_by('-date_submitted')
    return render(request, 'competition/vote.html', {'entries': entries})


def like_entry(request, entry_id):
    """
    Increments the like count for a specific entry
    """
    entry = get_object_or_404(Entry, id=entry_id)
    entry.likes += 1
    entry.save()
    return redirect('competition_vote')


def enter_competition(request):
    """
    Handles the entry form submission for the competition.
    """
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('competition_home')
    else:
        form = EntryForm()
    return render(request, 'competition/enter.html', {'form': form})
