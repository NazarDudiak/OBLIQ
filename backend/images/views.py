from PIL import Image, ExifTags
from io import BytesIO

from .models import OrderImage
from .serializers import OrderImageSerializer
from images.genToken import generate
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist


def check_orientation(img):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)

        return img
    except (AttributeError, KeyError, IndexError, TypeError):
        return img


def orderImageProcessor(request=None, order_id=None, action="view"):
    if action == "view":
        instance = OrderImage.objects.filter(order_id=order_id)
        if instance:
            serializer = OrderImageSerializer(instance=instance, many=True)
            return serializer.data[0]
        else:
            return None
    elif action == "add":
        instance = OrderImage.objects.filter(order_id=order_id)
        if len(instance) == 1:
            return False
        else:
            print("REQUEST DATA", dict(request.data))
            print("REQUEST FILE NAME", request.FILES['photo'])
            image = request.FILES["photo"]
            new_thumb_name = generate(16) + "-" + generate(16) + "-" + generate(16) + ".jpg"

            # Зберігаємо оригінальне ім'я файла
            original_image_name = image.name

            # Зменшуємо зображення
            img = Image.open(image)

            # Зберігаємо оріентацію зображення для того, щоб вона збереглася після конвертації
            img = check_orientation(img)

            # Отримати розміри зображення
            width, height = img.size

            # Зменшити ширину до 215 пікселів, пропорційно зменшити висоту
            new_width = 256
            new_height = int((height / width) * new_width)
            img = img.resize((new_width, new_height))

            # Зберігаємо зменшене зображення у BytesIO
            output = BytesIO()

            img.save(output, format='JPEG', quality=75)
            output.seek(0)

            # Серіалізуємо збережений об'єкт та додаємо його до списку збережених зображень
            instance = OrderImage(order_id=order_id,
                                  original_name=original_image_name,
                                  project_image_path=None)
            instance.save()
            # Зберігаємо зменшене зображення у базу даних з новим іменем
            thumb_image = InMemoryUploadedFile(
                output, 'ImageField', new_thumb_name, 'image/jpeg',
                output.getbuffer().nbytes, None
            )
            instance.project_image_path = thumb_image
            instance.save()
            serializer = OrderImageSerializer(instance=instance)
            saved_image = serializer.data
            return saved_image
    elif action == "patch":
        image_data = OrderImage.objects.filter(order_id=order_id).delete()
        if image_data[0] == 1:
            print("Deleted")
        else:
            print("Don't deleted")
        image = request.FILES["photo"]
        new_thumb_name = generate(16) + "-" + generate(16) + "-" + generate(16) + ".jpg"

        # Зберігаємо оригінальне ім'я файла
        original_image_name = image.name

        # Зменшуємо зображення
        img = Image.open(image)

        # Зберігаємо оріентацію зображення для того, щоб вона збереглася після конвертації
        img = check_orientation(img)

        # Отримати розміри зображення
        width, height = img.size

        # Зменшити ширину до 215 пікселів, пропорційно зменшити висоту
        new_width = 256
        new_height = int((height / width) * new_width)
        img = img.resize((new_width, new_height))

        # Зберігаємо зменшене зображення у BytesIO
        output = BytesIO()

        img.save(output, format='JPEG', quality=75)
        output.seek(0)

        # Серіалізуємо збережений об'єкт та додаємо його до списку збережених зображень
        instance = OrderImage(order_id=order_id,
                              original_name=original_image_name,
                              project_image_path=None)
        instance.save()
        # Зберігаємо зменшене зображення у базу даних з новим іменем
        thumb_image = InMemoryUploadedFile(
            output, 'ImageField', new_thumb_name, 'image/jpeg',
            output.getbuffer().nbytes, None
        )
        instance.project_image_path = thumb_image
        instance.save()
        serializer = OrderImageSerializer(instance=instance)
        saved_image = serializer.data
        return saved_image
    elif action == "delete":
        try:
            img = OrderImage.objects.filter(order_id=order_id).delete()
            # if deleted img[0] == 1 (True), else 0 (False)
            return img[0]
        except ObjectDoesNotExist:
            return False
    else:
        return False

# Create your views here.
