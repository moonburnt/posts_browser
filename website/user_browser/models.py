from django.db import models

# Create your models here.
class UsersModel(models.Model):
    """Model that holds user data"""

    # Overriding default id with one passed manually
    _id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    website = models.CharField(max_length=50, default="")

class PostsModel(models.Model):
    """Model that holds posts"""

    _id = models.IntegerField(primary_key=True)

    user = models.ForeignKey(UsersModel, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
