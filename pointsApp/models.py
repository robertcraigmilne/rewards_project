from django.db import models  #base Django Class to create application models
from django.urls import reverse #used to generate URLS by reversing URL patterns

class Members(models.Model):
  member_lastname = models.CharField(max_length=30)
  member_firstname = models.CharField(max_length=30)
  member_email = models.EmailField()
  #time_date = models.timestamp

#  def __str__(self):
#    return self.member_lastname
#    return self.member_firstname
#    return self.member_email

#  def get_absolute_url(self):
#    """Returns the url to access a particular instance of the model."""
#    return reverse('member-detail-view', args=[str(self.id)])

AFF_PDR_IND_CHOICES = [
    ('D', 'Domestic'),
    ('P', 'PDR'),
    ('A', 'Affiliate'),
]

class Resorts(models.Model):
  resort_num = models.CharField(max_length=30)
  resort_name = models.CharField(max_length=30)
  resort_aff_pdr_ind = models.CharField(max_length=1, choices = AFF_PDR_IND_CHOICES, default='D')

class Points(models.Model):
   member = models.ForeignKey(Members,on_delete=models.CASCADE) 
   resort_num = models.ForeignKey(Resorts,on_delete=models.CASCADE)
   resv_begin_date = models.DateField()
   resv_end_date = models.DateField()
   elig_rev = models.DecimalField(max_digits=11, decimal_places=2)  
   base_points = models.IntegerField()
   bonus_points = models.IntegerField()

