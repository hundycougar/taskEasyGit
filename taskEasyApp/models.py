from django.db import models
   # "taskName" character varying(254)[] COLLATE pg_catalog."default" NOT NULL,
   # "taskID" integer NOT NULL,
   # description character varying(1024) COLLATE pg_catalog."default",
   # completion timestamp with time zone[],
   # priority character(2) COLLATE pg_catalog."default",
   # CONSTRAINT "Tasks_pkey" PRIMARY KEY ("taskID")
# Create your models here.
class tasks(models.Model):
    taskName = models.CharField(max_length=254)
    taskID = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1024)
    completion = models.DateTimeField
    priority = models.CharField(max_length=2)
    class Meta:
        db_table = 'Tasks'
    def __str__(self):
        return self.taskName