from django.db import models
from datetime import datetime
 
class Posts(models.Model):

    title = models.CharField(verbose_name='Название', max_length=150, null=False, blank=False)
    pub_datetime = models.DateTimeField(verbose_name='Дата и время опубликования', null=False, blank=False, default=datetime.now()) # Date and time of publication
    content = models.TextField(verbose_name='Содержание', null=False, blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Посты'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'