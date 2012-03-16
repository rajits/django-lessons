========
Settings
========

.. code-block:: python

   DEFAULT_SETTINGS = {
       'RELATION_MODELS': [],
       'ACTIVITY_FIELDS': [],
       'LESSON_FIELDS': [],
       'JAVASCRIPT_URL': settings.MEDIA_URL + 'js/'
       'ASSESSMENT_TYPES': (
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
       ),
       'INTERNET_ACCESS_TYPES': (
           (1, 'No'),
           (2, 'Optional'),
           (3, 'Required'),
       ),
       'LEARNER_GROUP_TYPES': (
           (1, 'Advanced Placement'),
           (2, 'English Language Learners (ELL)'),
           (3, 'Gifted and Talented'),
           (4, 'International Baccalaureate'),
           (5, 'Special Education'),
           (6, 'Struggling Students'),
           (7, 'Adult Education'),
           (8, 'Continuing Education'),
       ),
       'PEDAGOGICAL_PURPOSE_TYPE_CHOICES': (
           (1, 'apply'),
           (2, 'develop'),
           (3, 'engage'),
       ),
       'STANDARD_TYPES': (
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
       ),
   }

Application Configuration
=========================

RELATION_MODELS
---------------

**Default:** ``[]``

A list of other models that a content producer can arbitrarily relate to these models. The contents of the list should be a string in the format ``'app.model'``.

ACTIVITY_FIELDS
---------------

**Default:** ``[]``

These fields are dynamically added to the admin of the Activity, but stored as generic relations as if they were a part of the above setting.

It consists of list of tuples where the first item in the tuple is the field name, and the second item is the ``'app.model'`` string.

LESSON_FIELDS
-------------

**Default:** ``[]``

These fields are dynamically added to the admin of the Lesson, but stored as generic relations as if they were a part of the above setting.

It consists of list of tuples where the first item in the tuple is the field name, and the second item is the ``'app.model'`` string.


JAVASCRIPT_URL
--------------

The path where the admin can load ``jquery-1.7.1.min.js``, ``genericcollections.js``, ``admin.js``.

Model Choices
=============

ASSESSMENT_TYPES
----------------

INTERNET_ACCESS_TYPES
---------------------

LEARNER_GROUP_TYPES
-------------------

PEDAGOGICAL_PURPOSE_TYPE_CHOICES
--------------------------------

STANDARD_TYPES
--------------
