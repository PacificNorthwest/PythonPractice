from flask import Flask
from flask_graphql import GraphQLView

def create_app():
    app = Flask(__name__)

    from app.schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    return app