# serlializers
# (여기는 필수항목리아고 뜨는 json문에 대한 응답을 보여주는 항목들이라고 생각하시면 됩니다~ 아 노드의 들어가는 것들을 나열한 거라고 생각하세요!)
import datetime
import uuid

from django.core.files.storage import default_storage
from rest_framework import serializers
import bcrypt
from neo4j import GraphDatabase, basic_auth

from backend import settings
from .models import USER, CARD, HAVE, RELATION  # models 모듈에서 USER, CARD, HAVE 클래스를 불러옵니다.


class UserRegisterSerializer(serializers.Serializer):
    user_uid = serializers.UUIDField(read_only=True)
    user_name = serializers.CharField(max_length=100)
    user_email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    user_phone = serializers.CharField(max_length=20, required=False)
    user_photo = serializers.ImageField(required=False, default='http://127.0.0.1:8000/static/person.png')
    is_user = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        attrs['user_uid'] = str(uuid.uuid4())
        # attrs['user_photo'] = ''
        if 'user_photo' in attrs:
            # Check if the 'user_photo' field has a file
            if hasattr(attrs['user_photo'], 'file'):
                # Save the file
                photo = attrs['user_photo']
                photo_name = default_storage.save(photo.name, photo)
                # Generate file URL
                photo_url = settings.MEDIA_URL + photo_name
                attrs['user_photo'] = photo_url
        if not attrs.get('user_photo'):  # 이미지를 제공하지 않았을 경우
            attrs['user_photo'] = '/static/person.png'  # 기본 이미지 경로를 사용
        attrs['is_user'] = True
        attrs['created_at'] = datetime.datetime.now()
        return attrs


class UserSerializer(serializers.Serializer):
    user_uid = serializers.UUIDField(required=False)
    user_name = serializers.CharField(max_length=100)
    user_email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    user_phone = serializers.CharField(max_length=20, read_only=True, required=False)
    user_photo = serializers.CharField(max_length=5000, allow_blank=True, required=False)
    is_user = serializers.BooleanField()
    created_at = serializers.DateTimeField()

    # updated_at = serializers.DateTimeField()


class LoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class CardSerializer(serializers.Serializer):
    card_uid = serializers.UUIDField(read_only=True)  # 추가
    card_name = serializers.CharField(max_length=100)
    card_email = serializers.EmailField()
    card_phone = serializers.CharField(max_length=20)
    card_intro = serializers.CharField(max_length=3000, allow_blank=True)
    card_photo = serializers.ImageField(required=False, default='http://127.0.0.1:8000/static/card.png')
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        attrs['card_uid'] = str(uuid.uuid4())
        # attrs['user_photo'] = ''
        if not attrs.get('card_photo'):  # 이미지를 제공하지 않았을 경우
            attrs['card_photo'] = '/static/card.png'  # 기본 이미지 경로를 사용
        attrs['update_at'] = datetime.datetime.now()
        attrs['created_at'] = datetime.datetime.now()
        return attrs


# class CardAddSerializer(serializers.Serializer):
#     card_uid = serializers.UUIDField(read_only=True)  # 추가
#     card_name = serializers.CharField(max_length=100)
#     card_email = serializers.EmailField()
#     card_phone = serializers.CharField(max_length=20)
#     card_intro = serializers.CharField(max_length=3000, allow_blank=True)
#     card_photo = serializers.CharField(max_length=5000)
#     created_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#
#     def validate(self, attrs):
#         attrs['card_uid'] = str(uuid.uuid4())
#         attrs['card_photo'] = ''
#         attrs['update_at'] = datetime.datetime.now()
#         attrs['created_at'] = datetime.datetime.now()
#         return attrs
class HAVESerializer(serializers.Serializer):
    have_uid = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class RelationSerializer(serializers.Serializer):
    relation_uid = serializers.UUIDField(read_only=True)
    relation_name = serializers.CharField(required=True)
    memo = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
