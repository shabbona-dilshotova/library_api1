from django.urls import path
import books.views
# from .views import BookListApi, book_list_view
from rest_framework.routers import SimpleRouter
from django.contrib.auth import get_user_model


router = SimpleRouter()
router.register('books', books.views.BookViewset, basename='books')
router.register('users', books.views.UserViewset, basename='users')

urlpatterns = [
    # # path('', books.views.BookListApi.as_view()),
    # path('books/', books.views.book_list_view),
    # path('<int:pk>/detail/', books.views.BookDetailView.as_view()),
    # # path('<int:pk>/delete/', books.views.BookDeleteApiView.as_view()),
    # # path('<int:pk>/update/', books.views.BookUpdateApiView.as_view()),
    #
    # # path('books/create/', books.views.BookCreateApiView.as_view()),
    #
    # path('list/create/', books.views.BookListCreateApiView.as_view()),
    # path('update/delete/<int:pk>/', books.views.BookUpdateDeleteApiView .as_view()),
    # path('<int:pk>/update/', books.views.BookUpdateApi.as_view()),
]

urlpatterns = urlpatterns + router.urls