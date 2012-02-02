
Integrations
============
* django-categories
* django-tagging
* django-textvariation

* Lessons will ultimately need to be collected in to Units.

* Add Lessons to Thinkfinity export

* Add these as content/ generic relations, although they will need to be considered as 'required' in the cms:

  * key_image (ForeignKey to NGPhoto)
  * resource carousel
  * promos

    * Share - Featured Service (in main nav)
    * right rail (2)
    * (below right rail, e.g. Sponsor)
    * bottom of page? (e.g. funders)

* categories

  * Subjects can be displayed inline, although it will be implemented using django-categories. There may be other fields that are displayed and implemented this way.
  * Tips will need to have categories

* Corey will implement these tables as lookups:

  * alternative_content_type (aka secondary_content_type)
  * disciplines (this will be used by tips, activities, and lessons)
  * grades (this will be used by activities, and lessons)
  * credits
  * categories (from edu_core)?

* Tagging - this app will need to be forked

  * Tagging will need the ability to insert its own field(s) in to a model (similar to django-categories)
  * 'Tag' model should have a 'public' flag?
  * Tags will be used by tips, activities and lessons
