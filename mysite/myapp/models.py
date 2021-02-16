from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     place = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     like_hot_dogs = models.BooleanField(default=False)
#     like_pizza = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s the user" % self.place.username

# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author.username) + " " + str(self.suggestion)

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(SuggestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author.username) + " " + str(self.comment)
