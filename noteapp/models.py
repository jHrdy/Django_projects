from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
       return f"{self.first_name} {self.last_name}"

class Notes(models.Model):

    SUBJECT_CHOICES = [             # musí se mapovat
        ('maths', 'Maths'),
        ('physics', 'Physics'),
        ('programming', 'Programming'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=60, blank=False, default="Untitled")
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='other')
    about = models.CharField(max_length=130, default='New notes, hope it helps :)')
    
    author = models.ForeignKey(
      "Author",
      on_delete=models.CASCADE,
      )
    file = models.FileField(blank=True, upload_to='notes/')

    def __str__(self):
        return self.title
