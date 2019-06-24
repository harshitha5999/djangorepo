from django import forms
from catalog.models import Book,Author,Genre

class BookForms(forms.Form):
    name = forms.CharField(label='Book Name',widget = forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    book_author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label='Author',widget = forms.Select(attrs={'name':'book_author','id':'book_author','class':'custom-select'}))
    purchase_date = forms.DateField(label='',widget = forms.DateInput(attrs={'placeholder':'Purchase Date','name':'purchase_date','id':'purchase_date','class':'form-control'}))
    #summary=forms.CharField(label='Summary',widget = forms.Textarea(attrs={'placeholder':'Summary','name':'summary','id':'summary','class':'form-control'}))
    #isbn = forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'ISBN Number','class':'form-control','name':'isbn','id':'isbn'}))
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)

class ModelBookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','genre','purchase_date','book_author')
        # fields = '__all__'

class SearchForm(forms.Form):
    q = forms.CharField(label='',
    widget = forms.TextInput(attrs={'maxlength':'30','placeholder':'Search','class':'form-control', 'minlength':'2'}))

# class CustomForms(forms.Form):
#     username = forms.CharField(
#         label = 'Username',
#         widget = forms.TextInput(
#             attrs = {'placeholder':'Your username',
#             'class':'form-control'
#             }
#         )
#     )
#     email = forms.EmailField(label="Your Email",widget=forms.EmailInput(attrs={'placeholder':'ac@mail.com','class':'form-control'}))

    #django project

