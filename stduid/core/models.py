from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class State(models.Model):
    state_uid = models.CharField(max_length=20,null=False, unique= True)
    state_name = models.CharField(max_length=100,unique=True, null=False)
    
    def save(self):
        temp = self.state_name.split(" ")
        if len(temp) > 1:
            temp = str(temp[0][:2])+str(temp[1][:2])
        else:
            temp = str(temp[0][:4])
            
        self.state_uid = "".join([str(ord(c)).lower() for c in temp]) 
        super().save(self)
    class Meta:
        
        verbose_name = _("State")
        verbose_name_plural = _("States")
        
    
        
        
    

class University(models.Model):
    uni_id = models.IntegerField(null=False)
    uni_uid = models.CharField(max_length=50,null=False, unique=True)
    uni_name = models.CharField(max_length=100, null=False)
    state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True)
    
    def save(self):
        self.uni_id = ''.join(str(ord(c)) for c in self.uni_name[:4])
        self.uni_uid = self.state.state_uid +"."+self.uni_id
        super().save(self)
    class Meta:
        
        verbose_name = _("University")
        verbose_name_plural = _("Universities")
        
    
        
class College(models.Model):
    college_id = models.IntegerField(null=False)
    college_uid = models.CharField(max_length=70, null=False,unique=True)
    college_name = models.CharField(max_length=100,null=False)
    college_detail = models.CharField(max_length=10000,blank=True,default="No Detail")
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    
    def save(self):
        self.college_id = ''.join(str(ord(c)) for c in self.college_name[:4])
        self.college_uid = self.university.uni_uid + "." + self.college_id
        super().save(self)
    class Meta:
        
        verbose_name = _("College")
        verbose_name_plural = _("Colleges")
    
class Student(models.Model):
    student_grno = models.IntegerField(null=False)
    student_uid = models.CharField(max_length=100, null=False, unique=True)
    student_name = models.CharField(max_length=100,null=False)
    student_detail = models.CharField(max_length=10000,blank=True,default="No detail")
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL,null=True)
    college = models.ForeignKey(College,on_delete=models.SET_NULL,null=True)
    
    class Meta:
        
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
    
    
    
    