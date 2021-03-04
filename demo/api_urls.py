from django.conf.urls import url
from core.views import UsersList

urlpatterns = [
    url(
        r'^users/$',
        UsersList.as_view(),
        name='user-list'
    ),
]
#urlpatterns +=[
#
#]
