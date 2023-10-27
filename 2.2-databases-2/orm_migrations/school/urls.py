from django.urls import path, include
import debug_toolbar

from school.views import students_list, add_relationships

urlpatterns = [
    path('', students_list, name='students'),
    path('add_relationships/', add_relationships, name='relationships'),
    path('__debug__/', include(debug_toolbar.urls)),
]

