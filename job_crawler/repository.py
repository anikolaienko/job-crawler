from sqlalchemy import create_engine, text

from config import db_connection

engine = create_engine(db_connection)

with engine.connect() as conn:
     result = conn.execute(text("SELECT * FROM test1"))
     print(result.all())
