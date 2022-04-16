class SQLAlchemySessionManager:
    def __init__(self, Session):
        self.Session = Session

    async def process_resource(self, req, resp, resource, params):
        resource.session = self.Session()
