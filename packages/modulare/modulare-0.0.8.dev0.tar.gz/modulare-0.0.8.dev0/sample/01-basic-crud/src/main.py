from modules.app.app_module import AppModule
from shared.factories.application_factory import ApplicationFactory
from shared.services.logger import console

def start():
    app = ApplicationFactory.create(AppModule)
    
    return app

app = start()

console.info('App started')