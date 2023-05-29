from django.db import models
from datetime import datetime

# Create your models here.
class songs(models.Model):
        title=models.CharField(max_length=30)
        image=models.ImageField(upload_to="images/")
        record=models.FieldFile(upload_to="document/")
        class mets:
                db_table="audio_store"