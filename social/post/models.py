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
        return self.likes.count()

    def get_dislikes(self):
        return self.dislikes.count()


class Like(models.Model):
    """ All likes posts """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name="Like user",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f'{self.user}\'s like to "{self.post.title}"'


class Dislike(models.Model):
    """ All dislikes for posts """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislikes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="dislikes",
        verbose_name="Dislike user",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f'{self.user}\'s dislike to "{self.post.title}"'
