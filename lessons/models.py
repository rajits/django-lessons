from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from settings import PEDAGOGICAL_PURPOSE_TYPE_CHOICES, RELATION_MODELS, RELATIONS

from BeautifulSoup import BeautifulSoup

def ul_as_list(html):
    soup = BeautifulSoup(html)
    return [li.contents[0] for li in soup('li')]

class AssessmentType(models.Model):
    name = models.CharField(max_length=128)
    thinkfinity_code = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class GroupingType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Material(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class PhysicalSpaceType(models.Model):
    name = models.CharField(max_length=128)
    is_default = models.NullBooleanField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class PluginType(models.Model):
    name = models.CharField(max_length=128)
    thinkfinity_code = models.CharField(max_length=128)
    source_url = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Skill(models.Model):
    parent_skill = models.ForeignKey('self')
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class TeachingApproachType(models.Model):
    name = models.CharField(max_length=128)
    is_default = models.NullBooleanField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class TeachingMethodType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class TechSetupType(models.Model):
    title = models.CharField(max_length=38)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]

TIP_TYPE_CHOICES = (
    ('T', 'Tip'),
    ('M', 'Modification'),
)

class Tip(models.Model):
    content_creation_time = models.DateTimeField()
    tip_type = models.PositiveSmallIntegerField(choices=TIP_TYPE_CHOICES)
    body = models.TextField()
    id_number = models.IntegerField()

class Activity(models.Model):
    assessment_type = models.ForeignKey(AssessmentType)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    id_number = models.IntegerField()
    pedagogical_purpose_type = models.SmallIntegerField(choices=PEDAGOGICAL_PURPOSE_TYPE_CHOICES)
    slug = models.SlugField(unique=True)
    subtitle_guiding_question = models.TextField()
    title = models.CharField(max_length=128)

   #Directions
    directions = models.TextField()
    tips = models.ManyToManyField(Tip)

   #Objectives
    learning_objectives = models.TextField()
    skills = models.ManyToManyField(Skill)
    teaching_approach_type = models.ForeignKey(TeachingApproachType)
    teaching_method_type = models.ForeignKey(TeachingMethodType)

   #Preparation
    accessibility_notes = models.TextField()
    materials = models.ManyToManyField(Material)
    grouping_type = models.ForeignKey(GroupingType)
    physical_space_types = models.ManyToManyField(PhysicalSpaceType)
    setup = models.TextField()
   #Required Technology
    plugin_types = models.ForeignKey(PluginType)
    tech_setup_types = models.ManyToManyField(TechSetupType)

   #Background & Vocabulary
    background_information = models.TextField()
    prior_knowledge = models.TextField()

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'Activities'

class Lesson(models.Model):
    ads_excluded = models.BooleanField()
    assessment = models.TextField()
    background_information = models.TextField()
    create_date = models.DateTimeField()
    description = models.TextField()
    duration_in_minutes = models.IntegerField()
    id_number = models.IntegerField()
    is_modular = models.BooleanField()
    last_updated_date = models.DateTimeField()
    learning_objectives = models.TextField()
    materials = models.ManyToManyField(Material)
    physical_space_type = models.ForeignKey(PhysicalSpaceType)
    slug = models.SlugField(unique=True)
    subtitle_guiding_question = models.TextField()
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]

    if RELATION_MODELS:
        def get_related_content_type(self, content_type):
            """
            Get all related items of the specified content type
            """
            return self.lessonrelation_set.filter(
                content_type__name=content_type)
        
        def get_relation_type(self, relation_type):
            """
            Get all relations of the specified relation type
            """
            return self.lessonrelation_set.filter(
                relation_type=relation_type)

    def get_activities(self):
        return [lessonactivity.activity for lessonactivity in self.lessonactivity_set.all()]

    def get_assessment(self):
        assessments = ul_as_list(self.assessments)

        for activity in self.get_activities():
            assessments += ul_as_list(activity.assessments)
        deduped_assessments = set(assessments)
        return list(deduped_assessments)

    def get_learning_objectives(self):
        return None

    def get_background_information(self):
        return None

#lessonrelation_limits = reduce(lambda x,y: x|y, RELATIONS)
class LessonRelationManager(models.Manager):
    def get_content_type(self, content_type):
        qs = self.get_query_set()
        return qs.filter(content_type__name=content_type)

    def get_relation_type(self, relation_type):
        qs = self.get_query_set()
        return qs.filter(relation_type=relation_type)

class LessonRelation(models.Model):
    lesson = models.ForeignKey(Lesson)
    content_type = models.ForeignKey(
        ContentType) # , limit_choices_to=lessonrelation_limits)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    relation_type = models.CharField("Relation Type", 
        max_length="200", 
        blank=True, 
        null=True,
        help_text="A generic text field to tag a relation, like 'primaryphoto'.")

    objects = LessonRelationManager()

    def __unicode__(self):
        out = "%s related to %s" % (self.content_object, self.collection)
        if self.relation_type:
            out += " as %s" % self.relation_type
        return out

class LessonActivity(models.Model):
    lesson = models.ForeignKey(Lesson)
    activity = models.ForeignKey(Activity)
    transition_text = models.TextField()

    class Meta:
        verbose_name_plural = 'Activities'
