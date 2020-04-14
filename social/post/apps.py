from django.apps import AppConfig
from django.db.models.signals import post_save


class PostConfig(AppConfig):
    name = "post"

    def ready(self):
        from post.signals import create_like_n_dislike

        post = self.get_model("Post")
        post_save.connect(create_like_n_dislike, sender=post)
