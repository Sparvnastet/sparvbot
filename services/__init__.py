def create_tables():
    from .whitelist.models import Whitelist
    Whitelist.create_table()
