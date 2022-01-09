from django import forms
from .models import profiles

class Profileregister(forms.ModelForm):
    class Meta:
        model = profiles
        fields = [
            "name","gender","dateOfBirth","maritalStatus","religion","image"
        ]

class Profileupdate(forms.ModelForm):
    class Meta:
        model = profiles
        fields = [
            "maritalStatus", "height", "image", "body_Type", "weight", "drink", "smoke", "motherTongue", "blood_group",
            "diet", "religion", "caste", "sub_caste",
            "placeOfBirth", "rassi", "education", "education_detail", "annual_income", "occupation_detail",
            "father_occupation", "mother_occupation", "no_of_brother",
            "no_of_sisters", "p_age_min", "p_age_max", "p_Marital_Status", "p_Body_Type", "p_Complexion", "p_Height",
            "p_Diet", "p_Manglik", "p_Religion", "p_Caste",
            "p_Mother_Tongue", "p_Education", "p_Country_Of_Residence", "p_State"

        ]