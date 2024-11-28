from django.db import models

class Spaces(models.Model):
    SpaceID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=255, null=True, blank=True)
    Type = models.CharField(max_length=50)
    Capacity = models.IntegerField(null=True, blank=True)
    Amenities = models.JSONField(null=True, blank=True)
    FloorPlan = models.IntegerField(null=True, blank=True)
    OccupationStatus = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'Spaces'

    def __str__(self):
        return self.Name


class PricePlan(models.Model):
    PriceID = models.AutoField(primary_key=True)
    Space = models.ForeignKey(Spaces, on_delete=models.CASCADE)
    Duration = models.CharField(max_length=50, null=True, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MembershipDiscount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    SeasonalDiscount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Price for {self.Space}"


class Member(models.Model):
    MemberID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField()
    Address = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    GST = models.CharField(max_length=20, null=True, blank=True)
    MembershipID = models.IntegerField(null=True, blank=True)
    LastLogin = models.DateTimeField(null=True, blank=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


class Booking(models.Model):
    BookingID = models.AutoField(primary_key=True)
    Space = models.ForeignKey(Spaces, on_delete=models.CASCADE)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Booking #{self.BookingID}"


class AccessControl(models.Model):
    AccessID = models.AutoField(primary_key=True)
    Member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    Space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    AccessType = models.CharField(max_length=50, null=True, blank=True)
    AccessStart = models.DateTimeField(null=True, blank=True)
    AccessEnd = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Access {self.AccessType}"


class Membership(models.Model):
    MembershipID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Benefits = models.JSONField(null=True, blank=True)
    AccessHours = models.CharField(max_length=50, null=True, blank=True)
    MonthlyFee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Validity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Name


class Invoice(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    IssueDate = models.DateField(null=True, blank=True)
    DueDate = models.DateField(null=True, blank=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    AdditionalFees = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Invoice #{self.InvoiceID}"


class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    PaymentDate = models.DateField(null=True, blank=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentMethod = models.CharField(max_length=50, null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    TransactionID = models.CharField(max_length=50, null=True, blank=True)
    LateFee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Payment #{self.PaymentID}"


class Feedback(models.Model):
    FeedbackID = models.AutoField(primary_key=True)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    Rating = models.IntegerField()
    Comments = models.TextField(null=True, blank=True)
    FeedbackDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Feedback #{self.FeedbackID}"


class Event(models.Model):
    EventID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)
    StartDateTime = models.DateTimeField(null=True, blank=True)
    EndDateTime = models.DateTimeField(null=True, blank=True)
    OrganizerID = models.IntegerField(null=True, blank=True)
    Venue = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Name
