from app.database import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("UPDATE alembic_version SET version_num = '4309e3cfb181'"))
    conn.commit()
    print('Alembic version reset to 4309e3cfb181')