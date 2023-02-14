from django.db import models


class Technology(models.Model):
    """Techologies in social-network
    """
    parent = models.ForeignKey(
        to='self', on_delete= models.SET_NULL, null=True, blank=True, related_name='childs'
    )
    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=100)
    content = models.TextField(default='')
    confirmed = models.BooleanField(default=False)

    @property
    def absolute_url(self):
        return f"/api/technology/{self.url}/"

    def __str__(self) -> str:
        return f"{self.parent if self.parent else ''}:{self.name}"