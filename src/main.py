import sys
from pathlib import Path
import psycopg


def find_project_root(current_file, marker="requirements.txt"):
    current_path = Path(current_file).resolve()
    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    return current_path.parent


project_root = find_project_root(__file__, marker="requirements.txt")
sys.path.insert(0, str(project_root))

from configs.config import PG_URL_CONFIG
from configs.postgresql_config import PostgreSQLConfig


test = PostgreSQLConfig(PG_URL_CONFIG["pg_url"], "symbol_db")

db_name = "dl_ckvn"
base_url = PG_URL_CONFIG["pg_url"]
db_name = "dl_ckvn"

with psycopg.connect(base_url + "/postgres", autocommit=True) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        if not cur.fetchone():
            cur.execute(f'CREATE DATABASE "{db_name}"')
            print(f"Database {db_name} created!")
        else:
            print(f"Database {db_name} already exists.")
