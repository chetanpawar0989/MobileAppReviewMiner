__author__ = 'Chetan'

from django.conf.urls import patterns, url

from ReviewMiner import views

urlpatterns = patterns('',
                       url(r'^$', views.appReview, name='appReview'),

                       url(r'^appreview$', views.appReview, name='appReview'),
                       url(r'^output$', views.appReviewUploadDone, name='output'),
                       url(r'^home$', views.appReview, name='home'),
                       url(r'^about$', views.about, name='about'),
                       )

