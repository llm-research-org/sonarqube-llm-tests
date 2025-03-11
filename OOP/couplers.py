class Repository:
    def find_by_id(self, id):
        # implementation
        return id

class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_repository(self):
        return self.repository

class Context:
    def __init__(self, service):
        self.service = service

    def use_case(self):
        # the following is a message chain
        entity = self.service.get_repository().find_by_id(1)
        print(entity)
