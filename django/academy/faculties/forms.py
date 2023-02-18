from django.forms import Form, CharField, IntegerField, ModelForm, ModelChoiceField

from faculties.models import Student, Group


class GroupAdd(Form):
    name = CharField(
        max_length=10,
        error_messages={
            'required': 'Please enter the group name',
            'max_length': 'Group name should be ten or less characters length',
        }
    )
    year = IntegerField(
        min_value=1,
        max_value=6,
        error_messages={
            'required': 'Please enter the group year of education',
            'min_value': 'Year of education should be between 1 and 6',
            'max_value': 'Year of education should be between 1 and 6',
        }
    )


class StudentAdd(ModelForm):
    rating = IntegerField(
        min_value=0,
        max_value=5,
        error_messages={
            'required': 'Please enter the group year of education',
            'min_value': 'Year of education should be between 0 and 5',
            'max_value': 'Year of education should be between 0 and 5',
        }
    )
    group = ModelChoiceField(
        empty_label='',
        queryset=Group.objects.all(),
    )

    class Meta:
        model = Student
        fields = ['group', 'name', 'surname', 'rating']

    def save(self, commit=True):
        for field in self.fields.values():
            print(field)
        return super().save(commit)

