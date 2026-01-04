from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/candidate/')
    
    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ensures one user can vote only once
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name} on {self.timestamp}"
