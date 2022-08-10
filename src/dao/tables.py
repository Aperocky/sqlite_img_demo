from sqlitedao import ColumnDict, SqliteDao

def get_dao(filename=None):
    if filename:
        DB_NAME = filename
    else:
        DB_NAME = "data.db"
    dao = SqliteDao.get_instance(DB_NAME)
    return dao

def create_tables():
    dao = get_dao()
    if not dao.is_table_exist("users"):
        create_users(dao)
    if not dao.is_table_exist("images"):
        create_images(dao)
    if not dao.is_table_exist("user_images"):
        create_user_images(dao)

def create_images(dao):
    # Create threads table
    columns = ColumnDict().add_column("ref", "text", "primary key")
    dao.create_table("images", columns)

def create_users(dao):
    columns = ColumnDict()\
        .add_column("user_id", "text", "primary key")\
        .add_column("completed", "integer")
    dao.create_table("users", columns)

def create_user_images(dao):
    columns = ColumnDict()\
        .add_column("pair_id", "text", "primary key")\
        .add_column("user_id", "text")\
        .add_column("ref", "text", "not null")\
        .add_column("score", "integer")
    index = {
        "user_id_index": ["user_id"],
        "image_ref_index": ["ref"]
    }
    dao.create_table("user_images", columns, index)
