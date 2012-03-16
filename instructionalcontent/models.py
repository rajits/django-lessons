#import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.utils.html import strip_tags

from settings import ASSESSMENT_TYPES, LEARNER_GROUP_TYPES, STANDARD_TYPES, PEDAGOGICAL_PURPOSE_TYPE_CHOICES, RELATION_MODELS, RELATIONS, INTERNET_ACCESS_TYPES

from audience.models import AUDIENCE_FLAGS
from BeautifulSoup import BeautifulSoup
from bitfield import BitField
from categories.models import Category, CategoryBase
from credits.models import CreditGroup
from edumetadata.models import *
from edumetadata.fields import HistoricalDateField
#from publisher import register
#from publisher.models import Publish
from education.edu_core.models import GlossaryTerm, Resource, ResourceCarouselSlide

def ul_as_list(html):
    soup = BeautifulSoup(html)
    return [li.contents[0] for li in soup('li')]

class TypeModel(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True
        ordering = ["name"]

    def __unicode__(self):
        return self.name

class GroupingType(TypeModel):
    pass

class Material(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class PhysicalSpaceType(TypeModel):
    is_default = models.NullBooleanField()

class PluginType(TypeModel):
    source_url = models.CharField(max_length=128)

class Skill(CategoryBase):
    appropriate_for = BitField(flags=AUDIENCE_FLAGS)
    url = models.CharField(max_length=128, blank=True, null=True)

class TeachingApproach(TypeModel):
    pass

class TeachingMethodType(TypeModel):
    pass

class TechSetupType(models.Model):
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]

TIP_TYPE_CHOICES = (
    (1, 'Tip'),
    (2, 'Modification'),
)

def truncate(string, limit):
    return string[:limit] + (string[limit:] and '...')

class Tip(models.Model):
    appropriate_for = BitField(flags=AUDIENCE_FLAGS)
    content_creation_time = models.DateTimeField(auto_now_add=True)
    id_number = models.CharField(max_length=5, blank=True, null=True)
    tip_type = models.PositiveSmallIntegerField(choices=TIP_TYPE_CHOICES)
    body = models.TextField()
    category = models.ForeignKey(EducationCategory, blank=True, null=True)

    class Meta:
        ordering = ["body"]

    def __unicode__(self):
        return truncate(strip_tags(self.body), 44)

class Standard(models.Model):
    appropriate_for = BitField(flags=AUDIENCE_FLAGS)
    definition = models.TextField('Standard text', null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    standard_type = models.CharField(max_length=14, choices=STANDARD_TYPES)
    state = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES)
    url = models.CharField(max_length=128, null=True, blank=True)
    when_updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    grades = models.ManyToManyField(Grade)

    def __unicode__(self):
        return "%s: %s" % (self.get_standard_type_display(), self.name)

    class Meta:
        ordering = ["name"]

class ContentManager(models.Manager):
    def get_published(self):
        qs = self.get_query_set()
        return qs.filter(published=True)

class Activity(models.Model):
    appropriate_for = BitField(flags=AUDIENCE_FLAGS, help_text='''Select the audience(s) for which this content is appropriate. Selecting audiences means that a separate audience view of the page will exist for those audiences.

Note that the text you input in this form serves as the default text. If you indicate this activity is appropriate for multiple audiences, you either need to add text variations or the default text must be appropriate for those audiences.''')
    title = models.TextField(help_text="GLOBAL: Use the text variations field to create versions for audiences other than the default.")
    ads_excluded = models.BooleanField(default=True, verbose_name="Are ads excluded?", help_text="If unchecked, this field indicates that external ads are allowed.")
    assessment = models.TextField()
    assessment_type = models.CharField(max_length=15, blank=True, null=True, choices=ASSESSMENT_TYPES)
    description = models.TextField()
    duration = models.IntegerField(verbose_name="Duration Minutes")
    extending_the_learning = models.TextField(blank=True, null=True)
    grades = models.ManyToManyField(Grade)
    id_number = models.CharField(max_length=10, help_text="This field is for the internal NG Education ID number. This is required for all instructional content.")
    is_modular = models.BooleanField(default=True, help_text="If unchecked, this field indicates that this activity should not appear as stand-alone outside of a lesson view.")
    learner_group = models.SmallIntegerField(blank=True, null=True, choices=LEARNER_GROUP_TYPES)
    notes_on_readability_score = models.TextField(blank=True, null=True, help_text="Use this internal-use only field to record any details related to the readability of reading passages, such as those on handouts. Include Lexile score, grade-level equivalent, and any criteria used to determine why a higher score is acceptable (proper nouns, difficult vocabulary, etc.).")
    pedagogical_purpose_type = models.SmallIntegerField(blank=True, null=True, choices=PEDAGOGICAL_PURPOSE_TYPE_CHOICES)
    published = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, help_text="The URL slug is auto-generated, but producers should adjust it if: a) punctuation in the title causes display errors; and/or b) the title changes after the slug has been generated.")
    standards = models.ManyToManyField(Standard)
    subjects = models.ManyToManyField(Subject, limit_choices_to={'parent__isnull': False}, verbose_name="Subjects and Disciplines")
    subtitle_guiding_question = models.TextField(verbose_name="Subtitle or Guiding Question")

   #Directions
    directions = models.TextField()
    tips = models.ManyToManyField(Tip, blank=True, null=True, verbose_name="Tips & Modifications")

   #Objectives
    learning_objectives = models.TextField(help_text="If this activity is part of an already-created lesson and you update the learning objectives, you must also also make the same change in lesson for this field.")
    skills = models.ManyToManyField(Skill, limit_choices_to={'parent__isnull': False})
    teaching_approaches = models.ManyToManyField(TeachingApproach)
    teaching_method_types = models.ManyToManyField(TeachingMethodType)

   #Preparation
    accessibility_notes = models.TextField(blank=True, null=True)
    materials = models.ManyToManyField(Material)
    grouping_types = models.ManyToManyField(GroupingType)
    other_notes = models.TextField(blank=True, null=True)
    physical_space_types = models.ManyToManyField(PhysicalSpaceType, blank=True, null=True)
    prior_activities = models.ManyToManyField('self', blank=True, null=True, verbose_name="Recommended Prior Activities")
    setup = models.TextField(blank=True, null=True)
   #Required Technology
    internet_access_type = models.CharField(max_length=8, choices=INTERNET_ACCESS_TYPES)
    plugin_types = models.ForeignKey(PluginType, blank=True, null=True)
    tech_setup_types = models.ManyToManyField(TechSetupType, blank=True, null=True)

   #Background & Vocabulary
    background_information = models.TextField(help_text="If this activity is part of an already-created lesson and you update the background information, you must also make the same change in lesson for this field.")
    prior_knowledge = models.TextField()

  # Credits, Sponsors, Partners
    credit = models.ForeignKey(CreditGroup, blank=True, null=True)

  # Content Related Metadata
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name="Primary Category", related_name="primary_category")
    categories = models.ManyToManyField(Category, blank=True, null=True, verbose_name="Secondary Categories", related_name="secondary_categories")

  # Time and Date Metadata
    geologic_time = models.ForeignKey(GeologicTime, blank=True, null=True)
    relevant_start_date = HistoricalDateField(blank=True, null=True)
    relevant_end_date = HistoricalDateField(blank=True, null=True)

    objects = ContentManager()

    def __unicode__(self):
        return strip_tags(self.title)
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'Activities'

class Vocabulary(models.Model):
    activity = models.ForeignKey(Activity)
    glossary_term = models.ForeignKey(GlossaryTerm)

    class Meta:
        verbose_name_plural = 'Vocabulary'

class QuestionAnswer(models.Model):
    activity = models.ForeignKey(Activity)
    question = models.TextField()
    answer = models.TextField()
    appropriate_for = BitField(flags=AUDIENCE_FLAGS, blank=True, null=True)

    def __unicode__(self):
        # truncate
        limit = 44
        return self.question[:limit] + (self.question[limit:] and '...')

class ResourceItem(models.Model):
    activity = models.ForeignKey(Activity)
    resource = models.ForeignKey(Resource, related_name='instructional_resource')

relation_limits = reduce(lambda x,y: x|y, RELATIONS)

class RelationManager(models.Manager):
    def get_content_type(self, content_type):
        qs = self.get_query_set()
        return qs.filter(content_type__name=content_type)

    def get_relation_type(self, relation_type):
        qs = self.get_query_set()
        return qs.filter(relation_type=relation_type)

class ActivityRelation(models.Model):
    activity = models.ForeignKey(Activity)
    content_type = models.ForeignKey(
        ContentType, limit_choices_to=relation_limits)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    relation_type = models.CharField("Relation Type",
        max_length="200",
        blank=True,
        null=True,
        help_text="A generic text field to tag a relation, like 'primaryphoto'.")

    objects = RelationManager()

    def __unicode__(self):
        out = "%s related to %s" % (self.content_object, self.activity)
        if self.relation_type:
            out += " as %s" % self.relation_type
        return out

class Lesson(models.Model): # Publish):
    title = models.TextField(help_text="GLOBAL: Use the text variations field to create versions for audiences other than the default.")
    ads_excluded = models.BooleanField(help_text="If unchecked, this field indicates that external ads are allowed.")
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    duration = models.IntegerField(verbose_name="Duration in Minutes")
    geologic_time = models.ForeignKey(GeologicTime, blank=True, null=True)
    id_number = models.CharField(max_length=10, help_text="This field is for the internal NG Education ID number. This is required for all instructional content.")
    is_modular = models.BooleanField(help_text="If unchecked, this field indicates that this lesson should NOT appear as stand-alone outside of a unit view.")
    last_updated_date = models.DateTimeField(auto_now=True)
    overview_rcslide = models.ForeignKey(ResourceCarouselSlide, null=True, blank=True, related_name="rc_slide")
    published = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True)
    secondary_types = models.ManyToManyField(AlternateType, blank=True, null=True, verbose_name="Secondary Content Types")
    slug = models.SlugField(unique=True, help_text="The URL slug is auto-generated, but producers should adjust it if: a) punctuation in the title causes display errors; and/or b) the title changes after the slug has been generated.")
    subtitle_guiding_question = models.TextField(verbose_name="Subtitle or Guiding Question")

  # Directions
    assessment = models.TextField(blank=True, null=True, help_text="This field is for a new, lesson-level assessment. It is not impacted by activity-level assessments.")

  # Objectives
    learning_objectives = models.TextField(blank=True, null=True, help_text='Click the "import text" link to import learning objectives from all activities in this lesson into this field and edit them.')

  # Preparation
    materials = models.ManyToManyField(Material, blank=True, null=True, help_text="This field is for additional, lesson-level materials a teacher will need to provide; for example, new materials needed in order to conduct the lesson-level assessment. Do not repeat activity-specific materials.")
    other_notes = models.TextField(blank=True, null=True, help_text="This field has multiple uses, but one possible use is to indicate the larger context into which the lesson fits. Example: This is lesson 1 in a series of 10 lessons in a unit on Europe.")
  # Background & Vocabulary
    background_information = models.TextField(blank=True, null=True, help_text='Producers can either copy/paste background information into this field, or click the "import text" link to import background information from all activities in this lesson into this field and edit them.') 

  # Credits, Sponsors, Partners
    credit = models.ForeignKey(CreditGroup, blank=True, null=True)

  # Global Metadata
    appropriate_for = BitField(flags=AUDIENCE_FLAGS, help_text='''Select the audience(s) for which this content is appropriate. Selecting audiences means that a separate audience view of the page will exist for those audiences. For a lesson, the only possible choices are Teachers and Informal Educators.

Note that the text you input in this form serves as the default text. If you indicate this activity is appropriate for both T/IE audiences, you either need to add text variations or the default text must be appropriate for for both audiences.''')

  # Time and Date Metadata
    relevant_start_date = HistoricalDateField(blank=True, null=True)
    relevant_end_date = HistoricalDateField(blank=True, null=True)

    objects = ContentManager()

    def __unicode__(self):
        return strip_tags(self.title)
    
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

    def get_accessibility(self, activities=None):
        accessibility_notes = []

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            accessibility_notes += ul_as_list(activity.accessibility_notes)
        deduped_notes = set(accessibility_notes)
        return list(deduped_notes)

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
        '''Used by the admin to import text'''
        bg_info = self.background_information

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            bg_info += activity.background_information
        return bg_info

    def get_materials(self, activities=None):
        materials = self.materials.all()

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            materials |= activity.materials.all()
        deduped_materials = set(materials)
        return list(deduped_materials)

    def get_other_notes(self, activities=None):
        other_notes = self.other_notes

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            other_notes += activity.other_notes
        return other_notes

    def get_physical_space(self, activities=None):
        physical_space_types = []

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            physical_space_types += activity.physical_space_types.all()
        deduped_physical_space_types = set(physical_space_types)
        return list(deduped_physical_space_types)

    def get_required_technology(self, activities=None):
        required_technology = []

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            if activity.plugin_types:
                required_technology += activity.plugin_types
            required_technology += activity.tech_setup_types.all()
        deduped_technology = set(required_technology)
        return list(deduped_technology)

    def get_setup(self, activities=None):
        setup = []

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            setup += ul_as_list(activity.setup)
        deduped_setup = set(setup)
        return list(deduped_setup)

    def get_subjects(self, activities=None):
        subjects = self.subjects.all()

        if activities is None:
            activities = self.get_activities()
        for activity in activities:
            subjects |= activity.subjects.all()
        deduped_subjects = set(subjects)
        return list(deduped_subjects)

    # this override is, unfortunately, copied from education.edu_core.models - raj
    def save(self):
        from education.edu_core.models import ResourceCarouselModuleType, ResourceCategoryType

        if not self.overview_rcslide:
            if not self.id:
                super(Lesson, self).save()

            name = "Overview Lesson %s" % self.id
            rcs_type = ResourceCarouselModuleType.objects.get(name="Overview Module")
            _rctype = ResourceCategoryType.objects.get(name="Websites")

            new_rcs = ResourceCarouselSlide.objects.create(
                    name=name,
                    title=name,
                    resource_carousel_module_type=rcs_type,
                    resource_category_type=_rctype)
            _ctype = ContentType.objects.get_for_model(Lesson)
          # new_rcs.object_id_order = u"%s-%s" % (_ctype.id, self.id)
            new_rcs.save()

            self.overview_rcslide = new_rcs
        super(Lesson, self).save()

class LessonRelation(models.Model):
    lesson = models.ForeignKey(Lesson)
    content_type = models.ForeignKey(
        ContentType, limit_choices_to=relation_limits)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    relation_type = models.CharField("Relation Type",
        max_length="200",
        blank=True,
        null=True,
        help_text="A generic text field to tag a relation, like 'primaryphoto'.")

    objects = RelationManager()

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
