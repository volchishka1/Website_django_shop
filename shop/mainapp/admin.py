from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *



class SneekersAdminForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px;">При загружке изображения с разрешением больше {}x{} оно будет обрезано</span>""".format(
                *Product.MAX_RESOLUTION))

#    def clean_image(self):
#        image = self.cleaned_data['image']
#        img = Image.open(image)
#        if image.size > Product.MAX_IMAGE_SIZE:
#            raise ValidationError('Размер изображения не должен превышать 3MB!')
#        if img.height < min_height or img.width < min_width:
#            raise ValidationError('Разрешение изображения меньше минимального!')
#        if img.height > max_height or img.width > max_width:
#        return image



class SneekersAdmin(admin.ModelAdmin):

    form = SneekersAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sneekers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class KedsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='keds'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Sneekers, SneekersAdmin)
admin.site.register(Keds, KedsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
