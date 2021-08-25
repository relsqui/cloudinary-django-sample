from django.forms import ModelForm
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField(options=dict(upload_preset=Photo.upload_preset_name))

class PhotoUnsignedDirectForm(PhotoForm):
    image = CloudinaryUnsignedJsFileField(Photo.upload_preset_name)
