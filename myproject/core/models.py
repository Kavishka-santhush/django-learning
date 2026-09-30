from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200)       # මාතෘකාව සඳහා
    description = models.TextField()               # විස්තරය සඳහා
    created_at = models.DateTimeField(auto_now_add=True) # හැදුණු දිනය සහ වෙලාව

    def __str__(self):
        return self.title