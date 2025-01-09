from django.http import JsonResponse
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

# 위 코드에서 UserListCreateView 클래스는 모든 사용자를 검색하고 새 사용자를 만들 수 있는 API를 정의합니다.
# UserRetrieveUpdateDestroyView 클래스는 특정 사용자를 검색, 수정, 삭제할 수 있는 API를 정의합니다.
class UserListView(APIView):

    # get 방식으로 users/ 에 접속할 경우 모든 유저를 보여주는 api를 생성합니다.
    # queryset은 db에서 모든 유저 정보를 가져오는 쿼리문을 자동으로 생성하고 실행하여 모든 유저 정보를 배열로 반환합니다.
    def get(self, request):
        queryset = User.objects.all()
        user_list = list()
        for user in queryset:
            user_list.append(UserSerializer(user).data)
        return JsonResponse(dict(status='ok', message='모든 유저', users=user_list))

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # models.py에 작성된 User에 대한 필드값을 사용자가 입력한 정보로 설정하여 객체를 생성합니다.
        user = User.objects.create(username=username, email=email, password=password)
        # db에 저장합니다.
        user.save()
        return JsonResponse(dict(status='ok', message='회원가입에 성공하였습니다'))


class UserDetailAPIView(APIView):

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        if user is not None:
            serializer = UserSerializer(user)
            user = serializer.data
            return JsonResponse(dict(status='ok', data=user))
        return JsonResponse(dict(status='error', message='요청을 찾을 수 없습니다.'))

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        if user is not None:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(dict(status='error', message='잘못된 요청입니다.'))
        return JsonResponse(dict(status='error', message='요청을 찾을 수 없습니다.'))

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        if user is not None:
            user.delete()
            return JsonResponse(dict(status='ok', message='삭제에 성공하였습니다.'))
        return JsonResponse(dict(status='error', message='요청을 찾을 수 없습니다.'))
