from django.db import models
from django.conf import settings


class Post(models.Model):
    """ Basic post model """

    # to_field=username is better verbose option, instead of using id's
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        to_field="username",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Edited at")
    title = models.CharField(max_length=150, verbose_name="Post title")
    body = models.TextField(verbose_name="Post body")

    def __str__(self):
        return str(self.title)

    def get_likes(self):
        return self.likes.users.count()

    def get_dislikes(self):
        return self.dislikes.users.count()


class Like(models.Model):
    """ Likes for post. Unique for each post. Counts by how many users left likes for post """

    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="likes")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="post_likes")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.post.title}'s like"


class Dislike(models.Model):
    """ Dislikes for post. Unique for each post. Counts by how many users left dislikes for post """

    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="dislikes")
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post_dislikes"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.post.title}'s dislike"
