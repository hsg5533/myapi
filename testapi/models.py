from django.db import models


# Create your models here.

# 위 코드에서 User 모델은 username, email, password, created_at 필드를 가지고 있습니다.
# __str__ 메서드는 User 객체를 출력할 때 사용됩니다.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
