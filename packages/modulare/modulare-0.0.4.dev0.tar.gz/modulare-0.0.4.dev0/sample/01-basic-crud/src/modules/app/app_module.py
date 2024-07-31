
from modules.partner.partner_module import PartnerModule
from shared.decorators.module_decorator import Module
from modules.app.app_controller import AppController

@Module({
    'imports': [ PartnerModule ],
    'controllers': [ AppController ]
})
class AppModule:
    pass