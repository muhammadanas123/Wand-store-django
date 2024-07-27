from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class WandVariety(models.Model):
  WAND_TYPE_CHOICE = [
    ('EL', 'ELM'),
    ('CH', 'CHERRY'),
    ('AL', 'ALDER'),
    ('CN', 'CHESTNUT'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='wands/')
  date_added = models.DateTimeField(default=timezone.now)
  description = models.TextField(default='')
  price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
  type = models.CharField(max_length=2, choices=WAND_TYPE_CHOICE)

  def __str__(self):
      return self.name


# one to many

class WandReview(models.Model):
  wand = models.ForeignKey(WandVariety, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return f'{self.user.username} review for {self.wand.name }'

# many to many

class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  wand_varieties = models.ManyToManyField(WandVariety, related_name='stores')

  def __str__(self):
      return self.name

# one to one

class WandCertificate(models.Model):
  wand = models.OneToOneField(WandVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_untill = models.DateTimeField()

  def __str__(self):
      return f'Certificate for {self.name.wand}'
