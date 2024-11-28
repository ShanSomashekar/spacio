from django import forms
from .models import *

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Spaces
        fields = '__all__'


class PricePlanForm(forms.ModelForm):
    class Meta:
        model = PricePlan
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class AccessControlForm(forms.ModelForm):
    class Meta:
        model = AccessControl
        fields = '__all__'


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
