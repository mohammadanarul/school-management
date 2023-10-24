import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    current_page = 1
    next_page = 2
    prev_page = 0

    def get_paginated_response(self, data):
        if self.request.query_params.get("page", None):
            self.current_page = int(self.request.query_params.get("page", None))
            self.next_page = self.current_page + 1
            self.prev_page = self.current_page - 1

        last_page = math.ceil(self.page.paginator.count / self.page.paginator.per_page)

        response = {
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "count": self.page.paginator.count,
            "limit": self.page.paginator.per_page,
            "current_page": self.current_page,
            "next_page": self.next_page,
            "prev_page": self.prev_page,
            "last_page": last_page,
            "results": data,
        }
        return Response(response)
