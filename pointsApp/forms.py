from django import forms
from pointsApp.models import Members, Resorts, Points

class MembersForm(forms.ModelForm):

  #This allows us to inherit the table format from the MODELS.py same as Members Class (table def)
  # careful those are dbl underscores
  class Meta:
    model = Members
    #fields = "__all__" #more control if you split the fields out
    fields = ('member_lastname', 'member_firstname', 'member_email')
    labels = {'member_lastname':'Members Lastname',
              'member_firstname':'Members Firstname',
              'member_email':'Members Email'}

class ResortsForm(forms.ModelForm):

  class Meta:
    model = Resorts
    fields = ('resort_num', 'resort_name', 'resort_aff_pdr_ind')
    labels = {'resort_num':'Resort Num',
              'resort_name':'Resort Name',
              'resort_aff_pdr_ind':'Type'}

class PointsForm(forms.ModelForm):
    member_id = forms.ModelChoiceField(queryset=Members.objects.all())
    resort_num_id = forms.ModelChoiceField(queryset=Resorts.objects.all())

class Meta:
    model = Points
    fields = ('member_id', 'resort_num_id','resv_begin_date','resv_end_date','elig_rev','base_points','bonus_points')
    #fields = ('resort__id', 'resv_begin_date','resv_end_date','elig_rev','base_points','bonus_points')
    labels = {'member_id':'Member Id',
              'resort_num_id':'Resort# ID',
              'resv_begin_date':'Resv Begin Date',
              'resv_end_date':'Resv End Date',
              'elig_rev':'Eligible Rev',
              'base_points':'Base Points',
              'bonus_points':'Bonus Points'}
