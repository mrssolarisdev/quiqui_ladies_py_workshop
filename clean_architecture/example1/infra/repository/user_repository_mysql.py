from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

# As an outer layer, there is no problem to use things from the lower layers. But the opposite shouldn't happen.
from domain.repository.user_repository_meta import UserRepositoryMeta
from domain.models.user import User
from infra.schemas.user_table import user_table

class UserRepositoryMySql(UserRepositoryMeta):
    def __init__(self):
        # Always following the pattern: dialect+driver://username:password@hostname:port/database_name
        self.engine = create_engine(
            f"mysql+mysqlconnector://{settings.database.USERNAME}:"
            f"{settings.database.PASSWORD}@{settings.database.HOST}:"
            f"{settings.database.PORT}/{settings.database.DATABASE}"
        )
        self.session_builder = sessionmaker(bind=self.engine)
        self.session = self.session_builder()

            
    async def add_new_user(self, user: User) -> User:
        with self.session as conn:
            conn.execute(
                user_table.insert(
                    first_name=user.first_name, 
                    last_name=user.last_name, 
                    user_name=user.user_name, 
                    status=user.status
                )
            )
            conn.commit()
