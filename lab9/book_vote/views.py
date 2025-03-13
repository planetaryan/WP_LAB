# book_vote/views.py
from django.shortcuts import render
from .forms import VoteForm
from .models import Vote

def vote(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            # Get the vote choice from the form
            vote_choice = form.cleaned_data['vote']

            # Update the vote count for the selected choice
            vote, created = Vote.objects.get_or_create(choice=vote_choice)
            vote.count += 1
            vote.save()

            return render(request, 'book_vote/results.html', {'vote': vote_choice})
    else:
        form = VoteForm()

    # Get the total votes and percentage for each choice
    total_votes = sum(vote.count for vote in Vote.objects.all())
    votes = Vote.objects.all()
    percentages = {vote.choice: (vote.count / total_votes * 100) if total_votes else 0 for vote in votes}

    return render(request, 'book_vote/vote.html', {'form': form, 'percentages': percentages})
