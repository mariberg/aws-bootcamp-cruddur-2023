from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from lib.db import db

class UserActivities:
  def run(user_handle):
   # try:
    # x-ray -----
    model = {
        'errors': None,
        'data': None
    }
    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      sql = db.template('users', 'show')
      results = db.query_object_json(sql,{'handle': user_handle})
    model['data'] = results
            
    # x-ray ----
#    subsegment = xray_recorder.begin_subsegment('mock-data')
      
#    dict = {
#        "now": now.isoformat(),
#        "result-size": len(model['data'])
#    }
      
#    subsegment.put_metadata('key', dict, 'namespace')  
#    xray_recorder.end_subsegment()
    
#  finally:
#    xray_recorder.end_subsegment()
        
    return model      