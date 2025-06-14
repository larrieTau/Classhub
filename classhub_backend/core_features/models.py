from django.db import models

# Create your models here.
class Student_Report(models.Model):
    #MVP
    pass

class Financial_report(models.Model):
    #mvp
    pass


class SMS_Notificaton(models.Model):
    #mvp
    pass

class Subject(models.Model):
#Should we really use this for mvp
    pass

class Announcement(models.Model):
    #mvp
    pass

class Exam(models.Model):
    #not mvp
    pass

class Health_Record(models.Model):
    #not mvp but it should be if we have nurses as one of the users we shall be beginning with 
    pass

class Grade(models.Model):
    #THis model is not clear what is grade going to be doing like what are its attributes 
    # OR is part of the student report model 
    pass

class Leave_Application(models.Model):
    # Explain this one as well such that we know if its mvp or not mvp
    pass

