from django.db import models


class Message(models.Model):
    name = models.CharField('名字', max_length=20, null=False, blank=False)
    email = models.EmailField('邮箱', null=True, blank=True)
    message = models.CharField('留言', max_length=500, null=False, blank=False)
    time = models.DateTimeField('留言时间', auto_now=True)
    emergency = models.BooleanField('emergency?', default=False)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Message, self).save(*args, **kwargs)


