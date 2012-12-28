from django.db import models

class Food(models.Model):
	Name = models.CharField(max_length = 30, unique = True)
	Histamine_max = models.FloatField(null = True, blank = True)
	Histamine_min = models.FloatField(null = True, blank = True)
	Cadaverine_max = models.FloatField(null = True, blank = True)
	Cadaverine_min = models.FloatField(null = True, blank = True)
	Putrescine_max = models.FloatField(null = True, blank = True)
	Putrescine_min = models.FloatField(null = True, blank = True)
	Spermidine_max = models.FloatField(null = True, blank = True)
	Spermidine_min = models.FloatField(null = True, blank = True)
	Spermine_max = models.FloatField(null = True, blank = True)
	Spermine_min = models.FloatField(null = True, blank = True)
	Agmatine_max = models.FloatField(null = True, blank = True)
	Agmatine_min = models.FloatField(null = True, blank = True)
	Thyramine_max = models.FloatField(null = True, blank = True)
	Thyramine_min = models.FloatField(null = True, blank = True)
	Phenylethylamine_max = models.FloatField(null = True, blank = True)
	Phenylethylamine_min = models.FloatField(null = True, blank = True)
	Dopamine_max = models.FloatField(null = True, blank = True)
	Dopamine_min = models.FloatField(null = True, blank = True)
	Serotonine_max = models.FloatField(null = True, blank = True)
	Serotonine_min = models.FloatField(null = True, blank = True)
	Noradrenaline_max = models.FloatField(null = True, blank = True)
	Noradrenaline_min = models.FloatField(null = True, blank = True)

	DAO_Blocker = models.NullBooleanField(null = True, blank = True)
	Hist_Liberator = models.NullBooleanField(null = True, blank = True)
	Gut_Diet = models.NullBooleanField(null = True, blank = True)
	XAllergy = models.NullBooleanField(null = True, blank = True)
	SIGHI_Classification = models.PositiveSmallIntegerField(null = True, blank = True)

	Kilojoule = models.PositiveIntegerField(null = True, blank = True)
	Gly_Index = models.PositiveIntegerField(null = True, blank = True)
	Carbohydrates = models.FloatField(null = True, blank = True)
	Fat = models.FloatField(null = True, blank = True)
	Protein = models.FloatField(null = True, blank = True)
	Fiber= models.FloatField(null = True, blank = True)
		
	Comments = models.CharField(max_length = 500, null = True, blank = True)

	Subfoods = models.ManyToManyField('self', blank=True, null=True, symmetrical = False)

	def __unicode__(self):
		return self.Name


class Exercise(models.Model):
	Name = models.CharField(max_length = 30)
	Description = models.CharField(max_length = 500, null = True, blank = True)
	Kilojoule_per_hour = models.PositiveIntegerField(null = True, blank = True)

	def __unicode__(self):
		return self.Name

class Condition(models.Model):
	Name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.Name

class Bodypart(models.Model):
	Name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.Name

class Med_Type(models.Model):
	Name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.Name

class Med_Wirkstoff(models.Model):
	Name = models.CharField(max_length = 100)
	Histamine_Liberator = models.NullBooleanField(null = True, blank = True)
	DAO_Blocker = models.NullBooleanField(null = True, blank = True)

	def __unicode__(self):
		return self.Name

class Medication(models.Model):
	Name = models.CharField(max_length = 30)
	Type = models.ForeignKey(Med_Type, null = True, blank = True)
	Wirkstoff = models.ManyToManyField(Med_Wirkstoff,null = True, blank = True)
	Amount = models.PositiveIntegerField(null = True, blank = True)

	def __unicode__(self):
		return self.Name

class Allergen(models.Model):
	Name = models.CharField(max_length = 30)

class Preparation(models.Model):
	Name = models.CharField(max_length = 30, blank = True, null = True)

	def __unicode__(self):
		return self.Name
	
class Blood_Pressure_Inst(models.Model):
	Date = models.ForeignKey('Diary')
	Time = models.TimeField()
	Sys = models.PositiveIntegerField()
	Dia = models.PositiveIntegerField()
	
class Temperature_Inst(models.Model):
	Date = models.ForeignKey('Diary')
	Time = models.TimeField()
	Temperature = models.PositiveIntegerField()
	
class Pulse_Inst(models.Model):
	Date = models.ForeignKey('Diary')
	Time = models.TimeField()
	Pulse = models.PositiveIntegerField()

class Diary(models.Model):
    Date = models.DateField()
    Day = models.PositiveIntegerField()

    Food = models.ManyToManyField(Food,through = 'Food_Inst', null = True, blank = True, symmetrical = False)
    Medication = models.ManyToManyField(Medication,through = 'Medication_Inst', null = True, blank = True, symmetrical = False)
    Exercise = models.ManyToManyField(Exercise,through = 'Exercise_Inst', null = True, blank = True, symmetrical = False)
    Allergen = models.ManyToManyField(Allergen,through = 'Allergen_Inst', null = True, blank = True, symmetrical = False)
    Condition = models.ManyToManyField(Condition,through = 'Condition_Inst', null = True, blank = True, symmetrical = False)

    Pulse = models.ManyToManyField(Pulse_Inst, null = True, blank = True, symmetrical = False)
    Blood_Pressure = models.ManyToManyField(Blood_Pressure_Inst, null = True, blank = True)
    Temperature = models.ManyToManyField(Temperature_Inst, null = True, blank = True)

    Insomnia = models.PositiveIntegerField(null = True, blank = True)
    Comments = models.CharField(max_length=500, null = True, blank = True)

    def __unicode__(self):
	return str(self.Date)
	
class Allergen_Inst(models.Model):
	Allergen = models.ForeignKey(Allergen)
	Date = models.ForeignKey(Diary)
	Time = models.TimeField()
	Strength = models.PositiveSmallIntegerField()

class Exercise_Inst(models.Model):
	Exercise = models.ForeignKey(Exercise)
	Date = models.ForeignKey(Diary)
	Time = models.TimeField()
	Minutes = models.PositiveIntegerField()

class Medication_Inst(models.Model):
	Medication = models.ForeignKey(Medication)
	Date = models.ForeignKey(Diary)
	Time = models.TimeField()
	Amount = models.PositiveIntegerField()

class Food_Inst(models.Model):
	Food = models.ForeignKey(Food)
	Date = models.ForeignKey(Diary)
	Time = models.TimeField()
	Amount = models.PositiveIntegerField()
	Fresh = models.NullBooleanField(default = True, blank = True, null = True)
	Preparation = models.ForeignKey(Preparation)
	Homemade = models.NullBooleanField(default = True, blank = True, null = True)
#	def __unicode__(self):
#		return str(self.Date.Date) + ": " + str(self.Amount) + " " + self.Food.Name
	
class Condition_Inst(models.Model):
	Condition = models.ForeignKey(Condition)
	Date = models.ForeignKey(Diary)
	Time = models.TimeField()
	Time_End = models.TimeField(blank = True, null = True)
	Poss_HIT_Symptome = models.NullBooleanField(null = True, blank = True)
	Strength = models.PositiveIntegerField()
	Locations = models.ManyToManyField(Bodypart, null = True, blank = True)



