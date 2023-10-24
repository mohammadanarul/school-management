from drf_yasg import openapi
from drf_yasg.inspectors import NotHandled, PaginatorInspector


class SwaggerCustomPaginatorInspector(PaginatorInspector):
    """Provides response schema pagination wrapping for django-rest-framework's LimitOffsetPagination,
    PageNumberPagination and CursorPagination
    """

    def fix_paginated_property(self, key: str, value: dict):
        # Need to remove useless params from schema
        value.pop("example", None)
        if "nullable" in value:
            value["x-nullable"] = value.pop("nullable")
        if key in {"next", "previous"} and "format" not in value:
            value["format"] = "uri"
        return openapi.Schema(**value)

    def get_paginated_response(self, paginator, response_schema):
        if hasattr(paginator, "get_paginated_response_schema"):
            paginator_schema = paginator.get_paginated_response_schema(response_schema)
            if paginator_schema["type"] == openapi.TYPE_OBJECT:
                properties = {
                    k: self.fix_paginated_property(k, v) for k, v in paginator_schema.pop("properties").items()
                }
                if "required" not in paginator_schema:
                    paginator_schema.setdefault("required", [])
                    for prop in ("count", "results"):
                        if prop in properties:
                            paginator_schema["required"].append(prop)
                return openapi.Schema(**paginator_schema, properties=properties)
            else:
                return openapi.Schema(**paginator_schema)

        return response_schema
