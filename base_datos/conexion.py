from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

<<<<<<< HEAD
DATABASE_URL = "mysql+pymysql://root:password@localhost/sis_marl_jal"
=======
DATABASE_URL = "mysql+pymysql://root@localhost/sis_marl_jal"
>>>>>>> Bugs

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
