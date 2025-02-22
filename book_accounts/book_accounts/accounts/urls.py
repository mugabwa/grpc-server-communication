from book_accounts.accounts.views import BookAccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', BookAccountViewSet, basename='account')
urlpatterns = router.urls
