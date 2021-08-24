from django.forms import ModelForm
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoDirectForm(PhotoForm):
    upload_preset_name = Photo.signed_upload_preset_name
    image = CloudinaryJsFileField(options=dict(upload_preset=upload_preset_name))

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "un" + Photo.signed_upload_preset_name
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
