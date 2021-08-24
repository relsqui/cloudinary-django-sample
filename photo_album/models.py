from django.db import models
from cloudinary.models import CloudinaryField
# Next two lines are only used for generating the upload preset sample name
# (Moved here from forms.py to avoid a circular import when using the name in both places)
from cloudinary.compat import to_bytes
import cloudinary, hashlib

"""
This is the main model in the project. It holds a reference to cloudinary-stored
image and contains some metadata about the image.
"""
class Photo(models.Model):
    ## Misc Django Fields
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)

    ## Points to a Cloudinary image
    signed_upload_preset_name = "signed_sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryField('image', upload_preset=signed_upload_preset_name)

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
