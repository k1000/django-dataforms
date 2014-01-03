from django.conf.urls import url, patterns

urlpatterns = patterns('',
    
    # dataform urls
    url(r'^build/$', 'dataforms.views.build', name="db_build"),
    url(r'^build/field/(?P<field>[\w]+)/$', 'dataforms.views.get_field'),
    
)
