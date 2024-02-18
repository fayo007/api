from . import serializers
from main import models

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status


@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, id):
    print(request.user)
    product = models.Product.objects.get(id=id)
    serializer = serializers.DetailProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    categorys = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, id):
    products = models.Product.objects.filter(category_id = id)
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def salomlash(request):
#     try:
#         ism = request.data['ism']
#         data = {
#             'data':f'Assalomu alaykum {ism}',
#             'status':200
#             }
#         return Response(data, status=status.HTTP_200_OK)
#     except:
#         data = {
#             'data':'Xatolik',
#             'status':400
#             }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)



# product:{
# 'id':1,
# 'name':'abc'
# }
# image:[
# {'image':...},
# {'image':...},
# {'image':...},
# ]

# product:{
# 'id':1,
# 'name':'abc',
# 'image':[{'image':...},{'image':...},{'image':...}]
# }