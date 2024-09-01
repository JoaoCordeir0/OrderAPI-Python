from sqlalchemy import create_engine
from src.database.Bases import Base
from sqlalchemy.orm import sessionmaker

class Engine:

    """NOTE: Classe para conexão com o banco de dados"""

    session = None

    def __init__(self) -> None:
        engine = create_engine('sqlite:///example.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_session(self):
        return self.session