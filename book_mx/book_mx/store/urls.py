from book_mx.store.views import BookViewSet, BookStoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'bookstores', BookStoreViewSet)
urlpatterns = router.urls