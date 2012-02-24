#import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.localflavor.us.us_states import STATE_CHOICES

from settings import PEDAGOGICAL_PURPOSE_TYPE_CHOICES, RELATION_MODELS, RELATIONS

from BeautifulSoup import BeautifulSoup
from edumetadata.models import *
#from publisher import register
#from publisher.models import Publish

ASSESSMENT_TYPES = (
    ('alternative', 'Alternative Assessment'),
    ('authentic', 'Authentic Assessment'),
    ('informal', 'Informal Assessment'),
    ('observation', 'Observation'),
    ('peer-evaluation', 'Peer Evaluation'),
    ('portfolio', 'Portfolio Assessment'),
    ('rubric', 'Rubric'),
    ('self', 'Self Assessment'),
    ('standardized', 'Standardized Testing'),
    ('testing', 'Testing'),
)

STANDARD_TYPES = (
    ('language', 'IRA/NCTE Standards for the English Language Arts'),
    ('social-studies', 'National Council for Social Studies Curriculum Standards'),
    ('geography', 'National Geography Standards'),
    ('science', 'National Science Education Standards'),
    ('art', 'National Standards for Arts Education'),
    ('history', 'National Standards for History'),
    ('math', 'NCTM Principles and Standards for School Mathematics'),
    ('ocean', 'Ocean Literacy Essential Principles and Fundamental Concepts'),
    ('state', 'TEST: State Standards'),
    ('econ', 'Voluntary National Content Standards in Economics'),
)

TEACHING_APPROACH_TYPES = (
    ('constructivist', 'constructivist'),
    ('inquiry', 'Inquiry-based learning'),
    ('interdisciplinary', 'Interdisciplinary'),
    ('for-use', 'Learning-for-use'),
    ('montessori', 'Montessori'),
    ('object', 'Object-based learning'),
    ('project', 'Project-based learning'),
    ('thematic', 'Thematic approach'),
)

def ul_as_list(html):
    soup = BeautifulSoup(html)
    return [li.contents[0] for li in soup('li')]

class GroupingType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

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
    parent_skill = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class TeachingMethodType(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

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
    content_creation_time = models.DateTimeField(auto_now_add=True)
    id_number = models.IntegerField(blank=True, null=True)
    tip_type = models.PositiveSmallIntegerField(choices=TIP_TYPE_CHOICES)
    body = models.TextField()
    category = models.ForeignKey(EducationCategory, blank=True, null=True)

    def __unicode__(self):
        # truncate
        limit = 44
        return self.body[:limit] + (self.body[limit:] and '...')

class Standard(models.Model):
    definition = models.TextField('Standard text', null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    standard_type = models.CharField(max_length=14, choices=STANDARD_TYPES)
    state = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
    url = models.CharField(max_length=128, null=True, blank=True)
    when_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Activity(models.Model):
    assessment = models.TextField()
    assessment_type = models.CharField(max_length=15, blank=True, null=True, choices=ASSESSMENT_TYPES)
    description = models.TextField()
    duration = models.IntegerField(verbose_name="Duration Minutes")
    grades = models.ManyToManyField(Grade)
    id_number = models.IntegerField(blank=True, null=True)
    pedagogical_purpose_type = models.SmallIntegerField(blank=True, null=True, choices=PEDAGOGICAL_PURPOSE_TYPE_CHOICES)
    slug = models.SlugField(unique=True)
    standards = models.ManyToManyField(Standard)
    subjects = models.ManyToManyField(Subject, verbose_name="Subjects and Disciplines")
    subtitle_guiding_question = models.TextField()
    title = models.CharField(max_length=128)

   #Directions
    directions = models.TextField()
    tips = models.ManyToManyField(Tip, blank=True, null=True)

   #Objectives
    learning_objectives = models.TextField()
    skills = models.ManyToManyField(Skill)
    teaching_approach_type = models.CharField(max_length=17, choices=TEACHING_APPROACH_TYPES)
    teaching_method_types = models.ManyToManyField(TeachingMethodType)

   #Preparation
    accessibility_notes = models.TextField(blank=True, null=True)
    materials = models.ManyToManyField(Material)
    grouping_types = models.ManyToManyField(GroupingType)
    other_notes = models.TextField(blank=True, null=True)
    physical_space_types = models.ManyToManyField(PhysicalSpaceType)
    setup = models.TextField(blank=True, null=True)
   #Required Technology
    plugin_types = models.ForeignKey(PluginType, blank=True, null=True)
    tech_setup_types = models.ManyToManyField(TechSetupType, blank=True, null=True)

   #Background & Vocabulary
    background_information = models.TextField()
    prior_knowledge = models.TextField()

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'Activities'

class Lesson(models.Model): # Publish):
    ads_excluded = models.BooleanField()
    assessment = models.TextField(blank=True, null=True)
    background_information = models.TextField(blank=True, null=True) 
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    duration = models.IntegerField(verbose_name="Duration in Minutes")
    geologic_time = models.ForeignKey(GeologicTime, blank=True, null=True)
    grades = models.ManyToManyField(Grade)
    id_number = models.IntegerField(blank=True, null=True)
    is_modular = models.BooleanField()
    last_updated_date = models.DateTimeField(auto_now=True)
    learning_objectives = models.TextField(blank=True, null=True)
    materials = models.ManyToManyField(Material, blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    physical_space_type = models.ForeignKey(PhysicalSpaceType, blank=True, null=True)
  # publish_date = models.DateTimeField(default=datetime.datetime.now)
    secondary_types = models.ManyToManyField(AlternateType, blank=True, null=True, verbose_name="Secondary Content Types")
    slug = models.SlugField(unique=True)
    subjects = models.ManyToManyField(Subject, blank=True, null=True)
    subtitle_guiding_question = models.TextField()
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]

  # class PublishingMeta:
  #     published_datefield = 'publish_date'

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

    # TODO
    def get_glossary(self):
        pass

    def get_learning_objectives(self, activities=None):
        objectives = ul_as_list(self.learning_objectives)

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            objectives += ul_as_list(activity.learning_objectives)
        deduped_objectives = set(objectives)
        return list(deduped_objectives)

    def get_background_information(self, activities=None):
        bg_info = self.background_information

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            bg_info += activity.background_information
        return bg_info

    def get_other_notes(self, activities=None):
        other_notes = self.other_notes

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            other_notes += activity.other_notes
        return other_notes

    def get_subjects(self, activities=None):
        subjects = self.subjects.all()

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            subjects |= activity.subjects.all()
        deduped_subjects = set(subjects)
        return list(deduped_subjects)

lessonrelation_limits = reduce(lambda x,y: x|y, RELATIONS)
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
        ContentType, limit_choices_to=lessonrelation_limits)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    relation_type = models.CharField("Relation Type", 
        max_length="200", 
        blank=True, 
        null=True,
        help_text="A generic text field to tag a relation, like 'primaryphoto'.")

    objects = LessonRelationManager()

    def __unicode__(self):
        out = "%s related to %s" % (self.content_object, self.lesson)
        if self.relation_type:
            out += " as %s" % self.relation_type
        return out

class LessonActivity(models.Model):
    lesson = models.ForeignKey(Lesson)
    activity = models.ForeignKey(Activity)
    transition_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Activities'

#register(Activity)
#register(Lesson)
