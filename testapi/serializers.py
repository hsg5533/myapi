from rest_framework import serializers
from .models import User

# 위 코드에서 UserSerializer 클래스는 User 모델에 대한 시리얼라이저입니다.
# Meta 클래스의 model 속성은 시리얼라이저가 사용할 모델을 지정합니다.
# fields 속성은 JSON으로 직렬화할 필드 목록을 지정합니다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'created_at')
