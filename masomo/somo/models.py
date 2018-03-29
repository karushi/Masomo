from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grade(models.Model):
  Name = models.CharField(max_length=25)
  description= models.CharField(max_length=150)
  grade = models.CharField(max_length=3)


  @classmethod
  def grade(cls):
      pass

  def delete_grade(self):
      self.remove()    

  def save_grade(self):
      self.save()  

class Student(models.Model):
  Name = models.CharField(max_length=25)
  AdmNo = models.IntegerField()
  student_grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
  Image = models.ImageField(upload_to='image/', null=True, blank=True)
  Form_class= models.CharField(max_length=10)
  
  
  
  @classmethod
  def Student(cls):
      pass

  def delete_images(self):
      self.remove()    

  def save_images(self):
      self.save()      

  @classmethod
  def search_by_name(cls,search_term):

    student =cls.objects.filter(Name__icontains=search_term)
    return student  
 

class Subject(models.Model):
  Name_subject = models.CharField(max_length=25)
  Student = models.ForeignKey(Student,on_delete=models.CASCADE)


@classmethod
def delete_subject(self):
      self.remove() 

def save_subject(self):
      self.save()      

class Fees(models.Model):
  Student = models.ForeignKey(Student,on_delete=models.CASCADE)
  fees = models.IntegerField(null=True)      
  
      