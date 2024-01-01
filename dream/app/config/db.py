from flask import current_app, g
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

def init_db():
    url_object = URL.create(
        "postgresql+psycopg2",
        username= current_app.config['DATABASE_USER'],
        password= current_app.config['DATABASE_PASSWORD'],
        host = current_app.config['DATABASE_HOST'],
        database = current_app.config['DATABASE_NAME']
    )

    engine = create_engine(url_object)

    g.db_session  = scoped_session(sessionmaker(autocommit=False,
                                    autoflush=False,
                                    bind=engine))

    g.base = declarative_base()
    g.base.query = g.db_session.query_property()
    import src.model.User
    g.base.metadata.create_all(bind=engine)

def close_db(e=None):
    db = g.pop('db_session', None)
    if db is not None:
        db.remove()

def init_app(app):
    app.teardown_appcontext(close_db)
    init_db()



