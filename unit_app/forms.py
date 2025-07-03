from django import forms

class UnitForm(forms.Form):
    CHOICES  = [
        ('none' , 'Select Unit'),
        ('cm_m' , 'Centimetres to Metres' ),
        ('cm_inches' , 'Centimetres to Inches'),
        ('m_km' , 'Metres to Kilometres'),
        ('km_mi' , 'Kilometres to Miles'),
        ('g_kg' , 'Grames to Kilogrames'),
        ('kg_to' , 'Kilogrames to Tonnes')
    ]

    number = forms.FloatField(required=True)
    options = forms.ChoiceField(choices=CHOICES , required = True , label='options')


    def CalculateUnit(self):

        unit = self.cleaned_data['number']
        operation = self.cleaned_data['options']

        if operation == 'none':
            result = 'Please Try Again....'

        elif operation == 'cm_m':
            conversion = unit/1000
            result = f"{unit}cm = {conversion}metres"

        elif operation == 'cm_inches':
            conversion = unit/2.54
            result = f"{unit}cm = {conversion}inches"

        elif operation == 'm_km':
            conversion = unit/1000
            result = f"{unit}m = {conversion}km"

        elif operation == 'km_mi':
            conversion = unit*1.609
            result = f"{unit}km = {conversion}miles"

        elif operation == 'g_kg':
            conversion = unit/1000
            result = f"{unit}g = {conversion}kg"

        elif operation == 'kg_to':
            conversion = unit/1000
            result = f"{unit}kg = {conversion}tonnes"

        else:
            result = f"Error.\n Please Try Again"

        return result