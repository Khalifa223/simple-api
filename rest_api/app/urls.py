from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookingViewSet, ContactViewSet, NewsletterViewSet

router = DefaultRouter()
router.register(r'books', BookingViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'newsletters', NewsletterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]