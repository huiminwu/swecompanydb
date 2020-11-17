from django.db import models

SPONSOR_TYPES = [
    ['NONE', 'Not a Sponsor'],
    ['BRONZE', 'Bronze'],
    ['SILVER', 'Silver'],
    ['GOLD', 'Gold']
]

REP_ROLES = [
    ['RECRUITER', 'Recruiter'],
    ['ENGINEER', 'Engineer'],
    ['OTHER', 'Other']
]

class Company(models.Model):
    name = models.CharField(max_length=100)
    sponsorship = models.CharField(choices=SPONSOR_TYPES, default='NONE', max_length=100) # level of sponsorship

    def __str__(self):
        return self.name
    
class CompanyRep(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    active = models.BooleanField(default=True) # status (active or not)
    main = models.BooleanField(default=False)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    role = models.CharField(choices=REP_ROLES, max_length=100)

    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name + ", " + str(self.company)