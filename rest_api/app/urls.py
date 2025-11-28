from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ContactViewSet, NewsletterViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'newsletters', NewsletterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]