
from modules.partner.partner_controller import PartnerController
from shared.decorators.module_decorator import Module

@Module({
    'controllers': [ PartnerController ]
})
class PartnerModule:
    pass