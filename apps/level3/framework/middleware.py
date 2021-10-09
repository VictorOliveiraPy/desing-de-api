from apps.level3.domain import DoesNotExist
from apps.level3.framework.http import NotFound


class FrameworkCommonExceptionHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exc):
        if isinstance(exc, DoesNotExist):
            return NotFound()
