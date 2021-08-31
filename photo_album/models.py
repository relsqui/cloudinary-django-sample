from django.db import models
from cloudinary.models import CloudinaryField

"""
This is the main model in the project. It holds a reference to cloudinary-stored
image and contains some metadata about the image.
"""
class Photo(models.Model):
    ## Misc Django Fields
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)
    default_options = dict(
        tags = ["new upload"],
        transformation = dict(
            width = 500,
            height = 500,
            crop = "limit"
        )
    )

    ## Points to a Cloudinary image
    image = CloudinaryField('image', **default_options)

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
