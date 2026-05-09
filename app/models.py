from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    category_id = Column(
    Integer,
    ForeignKey("categories.id", ondelete="SET NULL"),
    nullable=True
)
    updated_at = Column(
    TIMESTAMP(timezone=True),
    nullable=True,
    onupdate=func.now()
)

    # Foreign key (keyinroq User qo'shganda)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    owner = relationship("User", back_populates="posts")

    rating = Column(Integer, nullable=True, default=0)  # Yangi rating ustuni

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)   # ← YANGI
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    posts = relationship("Post", back_populates="owner")
    # User ga "is_active" ustuni:
    is_active = Column(Boolean, server_default="TRUE", nullable=False)


# models.py ga Category qo'shing:
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

# Keyin:
# alembic revision --autogenerate -m "add_categories_table"
# alembic upgrade head