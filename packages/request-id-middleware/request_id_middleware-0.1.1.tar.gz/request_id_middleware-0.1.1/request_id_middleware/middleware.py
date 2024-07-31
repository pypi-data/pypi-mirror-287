# request_id_middleware/middleware.py

import logging
import sentry_sdk
import threading

logger = logging.getLogger(__name__)

thread_local = threading.local()

class RequestIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request_id = request.META.get("HTTP_X_REQUEST_ID")
            if request_id:
                thread_local.request_id = request_id
                logger.info(f"X-Request-Id found: {request_id}")
                with sentry_sdk.configure_scope() as scope:
                    scope.set_tag("request_id", request_id)
        except Exception as e:
            logger.error(f"Failed to set request_id in Sentry scope: {e}")
        
        response = self.get_response(request)
        
        # Clean up thread-local storage
        if hasattr(thread_local, 'request_id'):
            del thread_local.request_id
        
        return response

    @staticmethod
    def get_request_id():
        return getattr(thread_local, 'request_id', None)
