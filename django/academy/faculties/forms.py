from django.forms import Form, CharField, IntegerField


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

