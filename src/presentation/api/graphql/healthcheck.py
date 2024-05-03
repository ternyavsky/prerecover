import strawberry
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class OkStatus:
    status: str = "OK"


OK_STATUS = OkStatus()


@strawberry.type
class GraphQLHealthQuery:
    @strawberry.field
    def get_status(self) -> OkStatus:
        return OK_STATUS


schema = Schema(query=GraphQLHealthQuery)
healthcheck_router = GraphQLRouter(schema)
