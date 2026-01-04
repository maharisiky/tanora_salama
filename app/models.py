from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=True)
    fb_id = models.IntegerField(null=True)
    visit = models.IntegerField(default=0)

class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('user', 'USER'), ('bot', 'CHATBOT')])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class QuickReply(models.Model):
    title = models.CharField(max_length=255)
    payload = models.CharField(max_length=255, unique=True)
    response_text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.payload})"

    class Meta:
        verbose_name = "Quick Reply"
        verbose_name_plural = "Quick Replies"