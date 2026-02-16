from django.db import models


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(self.text)


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self) -> str:
        """Return a string representation of the model."""
        if len(self.text) >= 50:
            return "..."
        return str(self.text)
