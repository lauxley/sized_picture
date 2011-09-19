from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models import CMSPlugin
from os.path import basename

class SizedPicture(CMSPlugin):
    """
    A Picture with or without a link
    and with fixed size
    """
    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    size = models.CharField(max_length=16, help_text=_("size of the image"), choices=settings.SIZED_PICTURE_SIZES)
    
    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"
