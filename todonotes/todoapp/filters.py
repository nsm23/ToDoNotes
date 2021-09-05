from django_filters import rest_framework

from todoapp.models import NoteModel


class NotesFilter(rest_framework.FilterSet):
    create_date = rest_framework.DateFromToRangeFilter(field_name='created_day')
    project = rest_framework.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = NoteModel
        fields = ['create_date', 'project']