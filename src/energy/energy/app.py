import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from energy import queries

schema = strawberry.Schema(query=queries.Query)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == "__main__":
    uvicorn.run(app, )
