from django.db import models


class Post(models.Model):
    # image
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    #tag
    #category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
    def __str__(self):
        return f"{self.title} - {self.id}"
