import os
import csv
import math
import geopy.distance
from myapi import settings
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

class Geo:

    @staticmethod
    def get_distance(pos1, pos2):
        return geopy.distance.distance(pos1, pos2)

    @staticmethod
    def get_radius_boundary(lat, lng, radius):
        lat_change = radius / 111.32
        lng_change = abs(math.cos(lat * (math.pi / 180)))

        return {
            "lat_min": lat - lat_change,
            "lng_min": lng - lng_change,
            "lat_max": lat + lat_change,
            "lng_max": lng + lng_change
        }


def load_csv(file):
    result = []

    with open(file, 'r', encoding='UTF8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            row = list(map(str.strip, row))  # trim
            result.append(row)

    result.pop(0)  # remove index

    return result


def load_address_db():
    file_path = os.path.join(settings.BASE_DIR, 'testapi/files/', 'db2.csv')
    lines = load_csv(file_path)
    result = []

    for line in lines:
        *address, latitude, longitude = line

        # 세부 행정구역 또는 좌표 정보가 없을 경우
        if not address[2] or not latitude or not longitude:
            continue

        result.append((' '.join(address).strip(),
                      float(latitude), float(longitude)))

    result.sort(key=lambda x: (x[1], x[2]))

    return result

g_db = load_address_db()  # initialize global variable

def search_address_from_position(latitude, longitude, radius):
    curr_position = (latitude, longitude)
    result = []

    for address, *address_position in g_db:
        dist = Geo.get_distance(curr_position, address_position)
        if dist < radius:
            result.append({'address':address})
    return result


class MapView(APIView):

    def get(self,request):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        km = request.query_params.get('km')
        output = search_address_from_position(float(lat), float(lng), int(km))
        return JsonResponse(dict(status='OK',
                                 data=output,
                                 message='조회 되었습니다.'), status=200)


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
