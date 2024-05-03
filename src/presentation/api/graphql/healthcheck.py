from fastapi import APIRouter, status
from dataclasses import dataclass
import strawberry
from strawberry.asgi import GraphQL
from strawberry.fastapi import GraphQLRouter
from strawberry import Schema


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
