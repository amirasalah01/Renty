from django.urls import path
from .views import (
    PropertyListCreateView,
    PropertyDetailView,
    MyPropertiesView,
    ReviewListCreateView,
    ReviewDetailView,
    PropertyRatingView
)

urlpatterns = [
    # Properties
    path('list/', PropertyListCreateView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('my/', MyPropertiesView.as_view(), name='my-properties'),

    # Reviews
    path('<int:property_id>/reviews/', ReviewListCreateView.as_view(), name='property-reviews'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/rating/', PropertyRatingView.as_view(), name='property-rating'),
]