from django.db import models

class Member(models.Model):
    MemberID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(unique=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    GST = models.CharField(max_length=20, null=True, blank=True)
    MembershipID = models.IntegerField(null=True, blank=True)
    PasswordHash = models.CharField(max_length=255)
    PasswordSalt = models.CharField(max_length=255)
    LastLogin = models.DateTimeField(null=True, blank=True)
    IsActive = models.BooleanField(default=True)
    AadharID = models.CharField(max_length=12, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'Members'  # Explicitly specify the existing table name

    def __str__(self):
        return self.Name
