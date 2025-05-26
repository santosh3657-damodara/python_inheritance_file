from django.shortcuts import render
from django.views.generic import View
from testapp.models import Student
import json
from testapp.utils import is_json
from testapp.mixins import SerializeMixin,HttpResponceMixin
from django.core.serializers import serialize
from testapp.forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(SerializeMixin,HttpResponceMixin,View):
    def get_obj_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except Student.DoesNotExist:
            s=None
        return s
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plase provide valid json data'})
            return self.render_to_http_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std=self.get_obj_by_id(id)
            if std is None:
                json_data=json.dumps({'msg':'no matched id is requeid'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.serilize([std,])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serilize(qs)
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not is_json:
            json_data=json.dumps({'msg':'plase provide valid json data'})
            return self.render_to_http_response(json_data,status=404)       
        stu_data=json.loads(data)
        form = StudentForm(stu_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'resourses created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=404)
        
    def put(self,request,*args,**kwargs):
        # emp=self.get_resourse_by_id(id)
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plase provide valid json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'plase provide valid id data properlly'})
            return self.render_to_http_response(json_data,status=404)
        stu=self.get_obj_by_id(id)
        
        original_data={
        'sname': stu.sname,
        'rollno': stu.rollno,
        'marks': stu.marks,
        'college': stu.college,
        'gf': stu.gf,
        'bf':stu.bf
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=stu)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'resourses updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=404)
        
    
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plase provide valid json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'plase provide valid delete id data'})
            return self.render_to_http_response(json_data,status=404)
        stu=self.get_obj_by_id(id)
        if stu is None:
            json_data=json.dumps({'msg':'plase provide not delete id data'})
            return self.render_to_http_response(json_data,status=404)
        status,deleted_item =stu.delete()
        if status==1:
            json_data=json.dumps({'msg':'deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'plase try agine later'})
        return self.render_to_http_response(json_data,status=500)
            
            
            
        
    

        
            
                
            
        
    
    
