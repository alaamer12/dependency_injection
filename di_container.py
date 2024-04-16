class DIContainer:
    def __init__(self):
        self._services = {}

    def register_service(self, name, service_cls):
        self._services[name] = service_cls

    def get_service(self, name):
        service_cls = self._services.get(name)
        if not service_cls:
            raise ValueError(f"Service '{name}' not registered.")
        return service_cls

    def create_instance(self, cls):
        args = []
        for param_name, param_type in cls.__init__.__annotations__.items():
            if param_name == 'return':
                continue
            if param_name in self._services:
                args.append(self.get_service(param_name))
            else:
                args.append(param_type())
        return cls(*args)
