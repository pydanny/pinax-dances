from django import forms
from django.utils.translation import ugettext as _

from dances.models import Dance

class DanceForm(forms.ModelForm):
    """Form for adding/editing a new dance
    
    """
    def __init__(self, user, group, *args, **kwargs):
        
        super(SampleForm, self).__init__(*args, **kwargs)
    
    def save(self, commit = True):
        return super(SampleForm, self).save(commit)
    
    class Meta:
        model = Dance
        fields = ('slug', 'title', 'description')
