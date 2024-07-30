import importlib
from fastapi import Depends


def get_service_instance():
    # TODO: To be fetched from config
    class_type = "RDS"
    class_map = {
        "RDS": "api.audit.RDS_service.rds_service.get_rds_service"
    }
    module_name, function_name = class_map[class_type].rsplit('.', 1)
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    return function


class DataStoreController:

    def __init__(self, service=Depends(get_service_instance())):
        self.service = service

    def get_service(self):
        return self.service
