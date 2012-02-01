
Models and Fields
=================

Note that these fields are considered core data, and should be isolated to this app. For additional data, or anything project-specific, check under the Integrations section.

* Material (e.g. pencils, atlas) - preparation for an activity or lesson

  * name

* AssessmentType (e.g. peer evaluation, testing, etc.)

  * name
  * thinkfinity_code

* These models may be replaced by choices in the settings file:

  * TeachingMethodType (e.g. Lecture, Demonstrations, etc)
  * GroupingType (e.g. One-to-one tutoring, Small-group instruction, etc)
  * TechSetupItem (e.g. Microphone, Scanner)

* TeachingApproachType (e.g. Project-based, Montessori, etc)

  * name
  * is_default (Boolean with null?)

* Skill (e.g. Media Literacy, Global Awareness)

  * parent_skill = ForeignKey
  * name
  * url = CharField

* PhysicalSpaceType (e.g. classroom, kitchen)

  * name
  * is_default

* PluginType (e.g. Active X, Flash) - is this even used anywhere?

  * name
  * thinkfinity_code? = CharField
  * source_url

* Tip

  * content_creation_time = DateTimeField
  * tip_type = SmallIntegerField (Tip=1, Modification=2)
  * body = TextField
  * (external_)id = IntegerField

* Activity

  * (external_)id = IntegerField
  * title = CharField
  * slug = SlugField
  * pedagogical_purpose_type = SmallIntegerField? (these values will be read from the settings file)
  * description = TextField
  * guiding_question (i.e. subtitle) = TextField
  * Directions
  
    * directions = TextField (I think we can also throw extending_the_learning in here)
    * tips

  * Objectives

    * learning_objectives = TextField
    * skills = ManyToManyField

  * Preparation

    * materials = ManyToManyField?
    * Required Technology

      * tech_setup_items = ManyToManyField
      * plugin_types = ForeignKey

    * physical_space = ForeignKey
    * setup = TextField
    * accessibility_notes = TextField
    * grouping_type = ForeignKey

  * Background & Vocabulary

    * background_information = TextField 
    * prior_knowledge = TextField

  * duration_minutes = IntegerField
  * teaching_approach_type = ForeignKey
  * teaching_method_type = ForeignKey

* Lesson

  * (external_id) = IntegerField
  * create_date = DateTimeField
  * last_updated_date = DateTimeField
  * title = CharField
  * slug = CharField
  * subtitle_guiding_question = CharField
  * description = TextField
  * duration_in_minutes = IntegerField
  * id_number = IntegerField
  * is_modular = BooleanField
  * ads_excluded = BooleanField
  * subjects = ManyToManyField (configurable from settings)
  * rollups

    * assessment = TextField
    * learning_objectives = TextField
    * background_information

  * Inline fields

    * Materials you provide
    * Activities
    * Content (generic) relations

* LessonActivity?

  * lesson = ForeignKey
  * activity = ForeignKey
  * transition_text = CharField? TextField?

* Unit
* Curriculum


Thoughts/ Notes/ Options
========================
Some of these tables could instead be stored as key-value pairs (e.g. material, pencil) in an intermediate table.
