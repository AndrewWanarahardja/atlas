from django.urls import path
from main.views import show_main, add_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product
from main.views import add_product_entry_ajax, delete_product_entry_ajax, edit_product_entry_ajax, get_product_entry_ajax
from main.views import login_ajax, register_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('delete-product-ajax/<uuid:product_id>/', delete_product_entry_ajax, name='delete_product_entry_ajax'),
    path('get-product-ajax/<uuid:product_id>', get_product_entry_ajax, name='get-product-ajax'),
    path('edit-product-ajax/<uuid:product_id>', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('login-ajax/', login_ajax, name='login-ajax'),
    path('register-ajax/', register_ajax, name='register-ajax'),
]