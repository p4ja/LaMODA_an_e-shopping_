from django.urls import path
from laModa import views

urlpatterns=[
    path('index/',views.index_page,name="index"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:cat_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:cat_id>/',views.delete_category,name="delete_category"),
    path('admin_page/',views.admin_page,name="admin_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('add_products/',views.add_products,name="add_products"),
    path('save_products/',views.save_products,name="save_products"),
    path('display_products/',views.display_products,name="display_products"),
    path('edit_products/<int:prod_id>/',views.edit_products,name="edit_products"),
    path('update_products/<int:prod_id>/',views.update_products,name="update_products"),
    path('delete_products/<int:prod_id>/',views.delete_products,name="delete_products"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('contact_delete/<int:cont_id>/',views.contact_delete,name="contact_delete")
]