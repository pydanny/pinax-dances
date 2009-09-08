from django import forms
from django.utils.translation import ugettext as _

from uni_form.helpers import FormHelper, Submit, Reset

from dances.models import Dance


class DanceForm(forms.ModelForm):
    """Form for adding/editing a new dance
    """
    
    # Attach a formHelper to your forms class.
    helper = FormHelper()

    # Add in a class and id
    helper.form_id = 'dance-form'
    helper.form_class = 'main-form'

    # add in a submit and reset button
    submit = Submit('submit','Submit')
    helper.add_input(submit)
    reset = Reset('reset','Reset')
    helper.add_input(reset)
    
    
    def __init__(self, creator, *args, **kwargs):
        
        super(DanceForm, self).__init__(*args, **kwargs)
    
    def save(self, commit = True):
        return super(DanceForm, self).save(commit)
    
    class Meta:
        model = Dance
        fields = ('slug', 'name', 'description')
