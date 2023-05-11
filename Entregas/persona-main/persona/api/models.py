from django.db import models

# Create your models here.
class Persona(models.Model):
    # id = models.AutoField(primary_key=True)
    # Django autodeclares the field id as a primary_key (if 
    # there are no pkeys)

    nombre = models.CharField(max_length=200,
                        help_text='Enter name')

    apellido = models.CharField(max_length=200,
                        help_text='Enter surname')
    
    email = models.EmailField(help_text='Enter email')

    def __str__(self):
        return "[" + str(self.id) +"]" + self.nombre + " " + self.apellido

    # Metadata
    class Meta:
        ordering = ['id']
    


