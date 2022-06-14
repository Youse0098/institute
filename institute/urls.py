from django.urls import path

from .views import (InstituteCreateView, InstituteDeleteView,
                    InstituteDetailView, InstituteListView,
                    InstituteUpdateView,TodayView,MonthView,UnpaidView,TotalView)

app_name = "institute"

urlpatterns = [
    path("list", InstituteListView.as_view(), name="list"),
    path("detail/<int:id>/", InstituteDetailView.as_view(), name="detail"),
    path("delete/<int:institute_id>/", InstituteDeleteView.as_view(), name="delete"),
    path("update/<int:id>/", InstituteUpdateView.as_view(), name="update"),
    path("create/", InstituteCreateView.as_view(), name="create"),
    path("today/<int:institute_id>/", TodayView.as_view(), name="today"),
    path("month/<int:institute_id>/", MonthView.as_view(), name="month"),
    path("unpaid/<int:institute_id>/",UnpaidView.as_view(),name="unpaid"),
    path("total/<int:institute_id>/",TotalView.as_view(),name="total"),

]
