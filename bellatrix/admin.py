from django.contrib import admin
from .models import WandVariety, WandCertificate, WandReview, Store

# Register your models here.

class WandReviewInline(admin.TabularInline):
  model = WandReview
  extra = 2

class WandVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [WandReviewInline]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('wand_varieties', )

class WandCertificateAdmin(admin.ModelAdmin):
  list_display =('wand', 'certificate_number')

admin.site.register(WandVariety, WandVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(WandCertificate, WandCertificateAdmin)
