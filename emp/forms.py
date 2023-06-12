from django import forms
class feedbackform(forms.Form):
    email = forms.EmailField(label="Enter your Email",max_length=50)
    name = forms.CharField(label="Enter Your Name", max_length=50, required=False)
    feedback = forms.CharField(label="your feedback", max_length=50, required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(feedbackform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'