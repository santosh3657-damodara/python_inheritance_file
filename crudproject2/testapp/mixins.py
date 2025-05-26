from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serilize(self,qs):
        json_data=serialize('json',qs)
        pdata=json.loads(json_data)
        final_list=[]
        for obj in pdata:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)
        return json_data
    
from django.http import HttpResponse 
class HttpResponceMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)

