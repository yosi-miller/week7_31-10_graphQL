from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from database.connection import DB_URL, db_session, init_db
from gql.query import Query

app = Flask(__name__)

schema = Schema(query=Query)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


with app.app_context():
    init_db()


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        '/graphql',
        schema=schema,
        graphiql=True,  # for GraphQL playground
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the session when the server disconnect"""
    db_session.remove()


if __name__ == '__main__':
    app.run()