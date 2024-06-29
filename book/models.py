from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70, null=False)
    description = models.TextField()
    auther = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.auther} \n"
                f"{self.title}")

    # def get_query(self):
    #     return self.objects.all()
