from django.db import models


class SearchQuery(models.Model):
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    max_capacity = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.from_city} to {self.to_city}"
