from django import forms

class userForms(forms.Form):    #making class which is used in views later

    #making two fields with input name
    #For changing type use widget
    #REQUIRED :not empty field msg type
    #also attributes name to change class name
    #textinput for text box
    #form-control apply bootstrap class
    #for making emailfield use EmailField
    #FOR OTHERS FIELD GO TO DJANGO OFFICIAL SITES
    num1=forms.CharField(label="value 1", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))  
    num3=forms.CharField(label="value 3", widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.EmailField()
