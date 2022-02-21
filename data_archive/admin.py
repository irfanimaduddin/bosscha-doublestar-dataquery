from django.contrib import admin
from import_export import resources
from import_export.admin import (
    ImportExportModelAdmin,
    ImportExportActionModelAdmin
)

from .models import *

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CrosscatResource(resources.ModelResource):
    class Meta:
        model = Crosscat


class MethodResource(resources.ModelResource):
    class Meta:
        model = Method


class ObjectcatResource(resources.ModelResource):
    class Meta:
        model = Objectcat


class ObserveddataResource(resources.ModelResource):
    class Meta:
        model = Observeddata


class ObserverResource(resources.ModelResource):
    class Meta:
        model = Observer


class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication


class CategoryAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Category Admin Page""" 
    verbose_name='Category'

    actions = None

    list_field = (
        'category_sign',
        'cat'
    )

    list_display = ( 
        'category_sign',
        'cat'
    )

    resource_class = CategoryResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class CrosscatAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Crosscat Admin Page""" 
    verbose_name='Cross Catalog'

    actions = None

    list_field = (
        'discoverer',
        'jasname',
        'ads',
        'bds',
        'ids',
        'wds',
    )

    list_display = ( 
        'discoverer',
        'jasname',
        'ads',
        'bds',
        'ids',
        'wds',
    )

    resource_class = CrosscatResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class MethodAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Method Admin Page""" 
    verbose_name='Observing Method'

    actions = None

    list_field = (
        'method_sign',
        'method',
    )

    list_display = ( 
        'method_sign',
        'method',
    )

    resource_class = MethodResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class ObjectcatAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Objectcat Admin Page""" 
    verbose_name='Object Catalog'

    actions = None

    list_field = (
        'crosscat_id',
        'ra',
        'decl',
        'gmaga',
        'gmagb',
        'gaia_sep',
        'gaia_pa',
        'probability',
        'category_id',
    )

    list_display = ( 
        'crosscat_id',
        'ra',
        'decl',
        'gmaga',
        'gmagb',
        'gaia_sep',
        'gaia_pa',
        'probability',
        'category_id',
    )

    resource_class = ObjectcatResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class ObserveddataAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Observeddata Admin Page""" 
    verbose_name='Observed Data'

    actions = None

    list_field = (
        'crosscat_id',
        'epoch',
        'data_pa',
        'data_sep',
        'count',
        'observer_id',
        'publication_id',
        'method_id',
    )

    list_display = ( 
        'crosscat_id',
        'epoch',
        'data_pa',
        'data_sep',
        'count',
        'observer_id',
        'publication_id',
        'method_id',
    )

    resource_class = ObserveddataResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class ObserverAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Observer Admin Page""" 
    verbose_name='Observer'

    actions = None

    list_field = (
        'observer_sign',
    )

    list_display = ( 
        'observer_sign',
    )

    resource_class = ObserverResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class PublicationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    """Class for Publication Admin Page""" 
    verbose_name='Publication'

    actions = None

    list_field = (
        'pub_sign',
    )

    list_display = ( 
        'pub_sign',
    )

    resource_class = PublicationResource

    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(Crosscat, CrosscatAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Objectcat, ObjectcatAdmin)
admin.site.register(Observeddata, ObserveddataAdmin)
admin.site.register(Observer, ObserverAdmin)
admin.site.register(Publication, PublicationAdmin)