from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('item_page/<product_id>/', views.item_page, name='item_page'),
    path('search/', views.search, name='search'),
    path('live_search/', views.live_search, name='live_search'),  # Add this lin
    path('sitemap.xml', views.sitemap_view)
]