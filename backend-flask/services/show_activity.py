from datetime import datetime, timedelta, timezone
class ShowActivity:
  def run(activity_uuid):
   
    sql = db.template('activities','show')
    results = db.query_object_json(sql,{
      'uuid': activity_uuid
    })
    return results