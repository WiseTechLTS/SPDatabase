from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from .forms import ProductUploadForm
# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


def index(request):
    data = Product.objects.all()
    context = {
        'data': data
    }
    return render(request, "display.html", context)


def uploadView(request):                                      
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ProductUploadForm()
    return render(request, 'upload.html', {'form': form})




@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_products(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        products = Product.objects.filter(user_id=request.user.id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
