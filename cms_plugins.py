from django.conf import settings
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from models import SizedPicture

class SizedPicturePlugin(CMSPluginBase):
    model = SizedPicture
    name = _("Sized Image")
    render_template = getattr(settings, 'SIZED_PICTURE_TEMPLATE', "cms/plugins/sized_picture.html")

    def render(self, context, instance, placeholder):
        instance.alt = settings.dbgettext(instance.alt)
        context.update({
            'picture':instance,
            'placeholder':placeholder
        })
        return context 

plugin_pool.register_plugin(SizedPicturePlugin)
