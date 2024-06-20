from rest_framework.pagination import PageNumberPagination

class GlobalPagination(PageNumberPagination):
    page_size = 5