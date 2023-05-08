import phonenumbers
from django import forms
from django.core.exceptions import ValidationError

from polls.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "phone"]

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            phone = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException:
            raise ValidationError('Phone isn`t correct')
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError('Phone isn`t correct')
        return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
