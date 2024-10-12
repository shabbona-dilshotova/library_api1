from rest_framework import serializers
from .models import Book
from django.contrib.auth import  get_user_model
from rest_framework.exceptions import ValidationError

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author, None')

        if not title .isalpha():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Kitob faqat harflardan iborat bo`lishi kerak '
                }
            )

        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob sarlovhasi va muallifi bir xil bo`lgan kitobni  '
                }
            )

    def validate_price(self, price):
        if price <0 or price > 99999999:
            raise ValidationError({
                'status': False,
                'message': "Narx no'to'g'ri kiritilgan"
            })

class CashSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=150)
    output = serializers.CharField(max_length=150)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
