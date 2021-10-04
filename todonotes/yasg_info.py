from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='ToDoNotes',
        default_version='0.0',
        description='Documentation ToDoNotes',
        contact=openapi.Contact(email='django@mail.ru'),
        license=openapi.License(name='NSM License'),

    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)