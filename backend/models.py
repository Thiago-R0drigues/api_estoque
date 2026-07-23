#define a estrutura da tabela
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(index=True)
    quantidade: Mapped[int] = mapped_column()