from rest_framework.pagination import PageNumberPagination


class FlowerPageNumberPagination(PageNumberPagination):
    page_size = 100
