from post.models import Like, Dislike


def create_like_n_dislike(sender, instance, created, **kwargs):
    """ When new post is created, just add like and dislike rows since they have
        OneToOneRelation, it will prepare post to get likes and dislikes. """
    if created:
        Like.objects.create(post=instance)
        Dislike.objects.create(post=instance)
