from distutils.command.upload import upload
from email import message
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    photo = models.ImageField(blank=True, upload_to = 'instagram/post/%y/%m/%d')
 

#Java의 toString
    def __str__(self):
        '''return f"Custom Post object ({self.id})" ->format 문법
        return "Custom Post object({})".format(self.id)'''
        return self.message
    
    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #      return len(self.message)
    # message_length.short_description = "메세지 글자 수"

class Comment(models.Model):    #필드명은 snake 케이스
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    #post.id 필드 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)