from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only =True)
    _id = serializers.SerializerMethodField(read_only =True)
    isAdmin = serializers.SerializerMethodField(read_only =True)


    class Meta:
        model = User
        fields =[ 'id', '_id','username','email', 'first_name','first_name','isAdmin' ]

    # def get_name(self,obj):
    #     name = obj.first_name
    #     if name == '':
    #         name = obj.email 
    #     return name   
    def get__id(self,obj):
        
        return obj.id 

    def get_isAdmin(self,obj): 
        
        return obj.is_staff 


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only =True)
    class Meta:
        model = User
        fields =[ 'id', '_id','username','email','isAdmin' , 'first_name' ,'last_name' ,'token']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
        
        