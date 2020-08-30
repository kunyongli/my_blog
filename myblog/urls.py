
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from.import views
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('articles/',include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^resume/$',views.resume),
    url(r'^$',article_views.article_list,name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)