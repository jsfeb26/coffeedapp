from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = [
    # Examples:
    # url(r'^$', 'coffeedapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
    url(r'location/create/$', coreviews.LocationCreateView.as_view()),
    url(r'search/$', coreviews.SearchListView.as_view()),
    url(r'location/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),
    url(r'location/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='reveiw_create'),
    url(r'location/(?P<pk>\d+)/review/udpate/$', coreviews.ReviewUpdateView.as_view(), name='reveiw_update'),
    url(r'entrance/$', coreviews.entrance),
]
