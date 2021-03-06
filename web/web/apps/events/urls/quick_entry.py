"""Url for the Zinnia quick entry view"""
from django.conf.urls import url
from django.conf.urls import patterns

from events.urls import _
from events.views.quick_entry import QuickEntry


urlpatterns = patterns(
    '',
    url(_(r'^quick-entry/$'),
        QuickEntry.as_view(),
        name='entry_quick_post')
)
