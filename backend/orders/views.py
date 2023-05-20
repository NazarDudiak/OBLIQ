from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser
from .serializers import OrderSerializer
from .models import Order

from images.views import orderImageProcessor


class OrdersListAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser,)

    @staticmethod
    def get(request):
        students = Order.objects.all()
        serializer = OrderSerializer(students, many=True)
        user_projects = []
        for project in serializer.data:
            image_data = orderImageProcessor(order_id=project["id"], action="view")
            project_for_save = dict(project)
            if image_data:
                project_for_save["photo"] = image_data["project_image_path"]
            else:
                project_for_save["photo"] = None
            user_projects.append(project_for_save)
        return Response(user_projects)

    @staticmethod
    def post(request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if "photo" in request.FILES:
                images_data = orderImageProcessor(request=request, order_id=int(serializer.data["id"]), action="add")
                if images_data:
                    order = Order.objects.get(id=serializer.data["id"])
                    order_serialized = OrderSerializer(order).data
                    order_serialized["photo"] = images_data
                    return Response(order_serialized, status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersDetailAPIView(APIView):
    @staticmethod
    def get_object(kwargs):
        try:
            pk = kwargs.get("order_id", None)
            if pk:
                return Order.objects.get(pk=pk)
            else:
                return None
        except ObjectDoesNotExist:
            return None

    def put(self, request, **kwargs):
        order = self.get_object(kwargs)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        order = self.get_object(kwargs)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        orderImageProcessor(request=request, order_id=int(order.id), action="delete")
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
