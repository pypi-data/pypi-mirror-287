from modules.app.app_service import AppService
from shared.decorators.route_decorator import route, register_routes
from shared.decorators.status_code_decorator import response_status_code

class AppController:
    def __init__(self, app_service: AppService):
        self.app_service = app_service
        self.router = register_routes(self)

    @route('get', '/')
    def health_check(self):
        return self.app_service.health_check()
