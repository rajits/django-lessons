
Approach
========

The education app will ultimately need to insert its own models into this module.

#. Core data, specific to instructional hierarchy - should be moved in to this module

   * Activities

     * EduBundle (ForeignKey, from BaseResourceCarousel)
     * GroupingType (ManyToManyField)
     * InternetAccessType (ForeignKey)
     * LearnerGroupType (ManyToManyField)
     * PedagogicalPurposeType (ForeignKey)
     * ResourceCarouselModuleType (ForeignKey, from BaseResourceCarousel)
     * TeachingApproachType (ManyToManyField)
     * TeachingMethodType (ManyToManyField)

   * Materials
   * Assessment types - only used by instructional hierarchy?

#. Core metadata, shared across education app - can be added using categories (once that module provides an abstract base class)

   * Subjects
   * Grades (used by both Activities and Lessons)
   * Eras - doesn't seem to actually be used anywhere?
   * Geologic times - ditto ^

#. Additional metadata - these can probably be added using generic relations

   * Credits - this will use a decorator, not generic relations (I think this also includes Logo and Promo, which are used by Activities)
   * Audience Appropriate For (also used by Activities?)
   * Photos
   * Resource carousel bundles?
   * Share this service sites - is this even being used?

Lessons and activities may be modular, or standalone. Activities that are not modular are only intended to be used as part of a Lesson and not by themselves. Lessons that are not modular are only inteded to be used as part of a Unit.
