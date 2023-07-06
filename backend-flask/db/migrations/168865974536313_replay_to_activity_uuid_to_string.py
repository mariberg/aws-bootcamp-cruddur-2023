from lib.db import db

class ReplayToActivityUuidToStringMigration:
  def migrate_sql():
    data = """
    ALTER TABLE activities
    ALTER COLUMN reply_to_activity_uuid TYPE text USING reply_to_activity_uuid::text;
    return data
    
  def rollback_sql():
    data = """
    ALTER TABLE activities
    ALTER COLUMN reply_to_activity_uuid TYPE integer USING reply_to_activity_uuid::integer;
    return data
    
  def migrate():
    db.query_commit(ReplayToActivityUuidToStringMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(ReplayToActivityUuidToStringMigration.rollback_sql(),{
    })
    
migration = ReplayToActivityUuidToStringMigration