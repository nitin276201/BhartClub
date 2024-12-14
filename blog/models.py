from django.db import models

class Post(models.Model):
    app_name = models.CharField(max_length=200)
    invite_code = models.CharField(max_length=200)
    app_size = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.app_name
