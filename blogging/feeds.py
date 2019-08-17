from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Updates"
    link = "/latest/feed/"
    description = "Updates on changes and additions to my blog."

    def items(self):
        return Post.objects.order_by('-published_date')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])