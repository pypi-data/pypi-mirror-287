from modules.partner.dto.create_partner_dto import CreatePartnerDTO
from modules.partner.dto.update_partner_dto import UpdatePartnerDTO
from modules.partner.partner_service import PartnerService
from modulare.decorators import response_status_code, route, register_routes

# from modulare.http.decorators import module_decorator, route_decorator, status_code_decorator

# from shared.decorators.enums.status_code_decorator_enum import StatusCode
# from shared.decorators.route_decorator import register_routes, route
# from shared.decorators.status_code_decorator import response_status_code

class PartnerController:
    def __init__(self, partner_service: PartnerService):
        self.partner_service = partner_service
        self.router = register_routes(self)

    @route('post', '/partner')
    @response_status_code(StatusCode.CREATED)
    async def create(self, create_partner_dto: CreatePartnerDTO):
        return await self.partner_service.create(create_partner_dto)
    
    @route('patch', '/partner')
    async def update(self, update_partner_dto: UpdatePartnerDTO):
        return await self.partner_service.update(update_partner_dto)
    
    @route('delete', '/partner/{id}')
    async def remove(self, id: int):
        return await self.partner_service.remove(id)
    
    @route('get', '/partner')
    async def findAll(self):
        return await self.partner_service.findAll()
    
    @route('get', '/partner/{id}')
    async def findOne(self, id: int):
        return await self.partner_service.findOne(id)

        