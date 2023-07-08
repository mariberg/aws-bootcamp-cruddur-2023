from lib.db import db

class ReplyToActivityUuidStringMigration:
  def migrate_sql():
    data = """
    """
    return data
    
  def rollback_sql():
    data = """
    """
    return data
    
  def migrate():
    db.query_commit(ReplyToActivityUuidStringMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(ReplyToActivityUuidStringMigration.rollback_sql(),{
    })
    
migration = ReplyToActivityUuidStringMigration