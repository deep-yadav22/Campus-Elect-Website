from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Candidate, Vote
from .forms import VoteForm

@login_required
def vote_page(request):
    if Vote.objects.filter(user=request.user).exists():
        messages.warning(request, "You have already voted!")
        return redirect('results')

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            Vote.objects.create(user=request.user, candidate=candidate)
            messages.success(request, f"You voted for {candidate.name}.")
            return redirect('results')
    else:
        form = VoteForm()

    candidates = Candidate.objects.all()
    return render(request, 'vote_page.html', {'form': form, 'candidates': candidates})

def results_page(request):
    candidates = Candidate.objects.all()
    results = {candidate: Vote.objects.filter(candidate=candidate).count() for candidate in candidates}
    return render(request, 'results_page.html', {'results': results})

def candidates_page(request):
    candidates = Candidate.objects.all()
    return render(request,'candidate.html',{"candidates":candidates})