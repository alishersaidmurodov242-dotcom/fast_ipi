from app.database import engine
from sqlalchemy import text, inspect

# Check existing tables
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Existing tables:", tables)

# Check posts table structure if it exists
if 'posts' in tables:
    columns = inspector.get_columns('posts')
    print("\nPosts table columns:")
    for col in columns:
        print(f"  {col['name']}: {col['type']} (nullable: {col['nullable']})")

# Check users table structure if it exists
if 'users' in tables:
    columns = inspector.get_columns('users')
    print("\nUsers table columns:")
    for col in columns:
        print(f"  {col['name']}: {col['type']} (nullable: {col['nullable']})")