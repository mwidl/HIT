from inputs.models import Diary
from inputs.models import Allergen
from inputs.models import Food
from inputs.models import Preparation
from inputs.models import Food_Inst
from inputs.models import Condition 
from inputs.models import Condition_Inst
from inputs.models import Bodypart
from inputs.models import Exercise 
from inputs.models import Exercise_Inst
from inputs.models import Medication
from inputs.models import Medication_Inst
from inputs.models import Med_Type
from inputs.models import Med_Wirkstoff
from inputs.models import Pulse_Inst
from inputs.models import Blood_Pressure_Inst
from inputs.models import Temperature_Inst
from django.contrib import admin

class FoodAdmin(admin.ModelAdmin):
	#list_display = ('Name', 'SIGHI_Classification','Histamine_min','Histamine_max','Putrescine_min','Putrescine_max','Thyramine_min','Thyramine_max','Serotonine_min','Serotonine_max','Comments','Kilojoule')
	list_display = ('Name','Histamine_min','Histamine_max', 'Kilojoule')
	filter_horizontal = ('Subfoods',)
	search_fields = ('Name',)
	#list_editable = ('SIGHI_Classification','Histamine_min','Histamine_max','Putrescine_min','Putrescine_max','Thyramine_min','Thyramine_max','Serotonine_min','Serotonine_max','Comments','Kilojoule')
	list_editable = ('Kilojoule',)

class PreparationAdmin(admin.ModelAdmin):
	list_display = ('Name',)

class Food_InstAdmin(admin.ModelAdmin):
	list_display = ('Date', 'Time','Food','Amount')
	list_filter = ('Date', 'Time','Food')
	save_as = True

class AllergenAdmin(admin.ModelAdmin):
	list_display = ('Name',)

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ('Name',)

class Exercise_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Exercise','Minutes')

class ConditionAdmin(admin.ModelAdmin):
	list_display = ('Name',)
	search_fields = ('Name',)

class Condition_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Condition','Strength')
	list_filter = ('Date', 'Time','Condition')
	save_as = True
	filter_horizontal = ('Locations',)

class Medication_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Medication')
	list_filter = ('Date', 'Time','Medication')
	save_as = True

class BodypartAdmin(admin.ModelAdmin):
	list_display = ('Name',)
	search_fields = ('Name',)

class MedicationAdmin(admin.ModelAdmin):
	list_display = ('Name',)
#	raw_id_fields = ('Type','Wirkstoff')
	#filter_vertical = ('Wirkstoff',)

class Med_WirkstoffAdmin(admin.ModelAdmin):
	list_display = ('Name',)

class Med_TypeAdmin(admin.ModelAdmin):
	list_display = ('Name',)

class DiaryAdmin(admin.ModelAdmin):
	list_display = ('Date','Day','Insomnia')
	exclude = ('Pulse','Blood_Pressure','Temperature')
	save_as = True

class Pulse_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Pulse')
	save_as = True

class Blood_Pressure_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Sys','Dia')
	save_as = True

class Temperature_InstAdmin(admin.ModelAdmin):
	list_display = ('Date','Time','Temperature')
	save_as = True

admin.site.register(Diary,DiaryAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Food_Inst,Food_InstAdmin)
admin.site.register(Condition,ConditionAdmin)
admin.site.register(Condition_Inst,Condition_InstAdmin)
admin.site.register(Bodypart,BodypartAdmin)
admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Exercise_Inst,Exercise_InstAdmin)
admin.site.register(Medication,MedicationAdmin)
admin.site.register(Medication_Inst,Medication_InstAdmin)
admin.site.register(Med_Type,Med_TypeAdmin)
admin.site.register(Med_Wirkstoff,Med_WirkstoffAdmin)
admin.site.register(Pulse_Inst, Pulse_InstAdmin)
admin.site.register(Blood_Pressure_Inst, Blood_Pressure_InstAdmin)
admin.site.register(Temperature_Inst, Temperature_InstAdmin)
admin.site.register(Preparation,PreparationAdmin)



