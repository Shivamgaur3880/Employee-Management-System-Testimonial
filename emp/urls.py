from django.contrib import admin
from django.urls import path,include
from emp import views

urlpatterns = [

  # path('',views.emp_home,name='home'),
  path('',views.emp_home),
  path('add-emp/',views.add_emp),
  path('view-emp/',views.view_emp),
  path('feedback-emp',views.feedback_emp),
  path('onlyview-emp/',views.only_view),
  path('delete-emp/<int:emp_id>/',views.delete_emp),
  path('update-emp/<emp_id>/',views.update_emp),
  path('do-update-emp/<emp_id>',views.do_update_emp),
  path('testimonial/',views.testimonial_fu),
  path('feedback',views.feedback_fu),
]