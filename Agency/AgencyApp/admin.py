from django.contrib import admin
from django.utils.timezone import now

from .models import RealEstate, Agent, Characteristic

# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('surname',)
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True



class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('location',)

    #moze da dodade samo agent
    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    # automaticaaly assigning agents
    def save_model(self, request, obj, form, change):
        super(RealEstateAdmin, self).save_model(request, obj, form, change)
        if not change:
            agent = Agent.objects.filter(user=request.user).first()
            if agent:
                obj.save()
                obj.agents.add(agent)
        if obj.sold.exists():
            for agents in obj.agent.all():
                agents.sales_number += 1

    def has_delete_permission(self, request, obj=None):
        if obj and obj.characteristics.exists():
            return False
        return True

    #change only for assigned agents
    def has_change_permission(self, request, obj=None):
        return obj and obj.agent.filter(user=request.user).exists()

    def has_view_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        qs = super(RealEstateAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(date=now().date())
        return qs


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)