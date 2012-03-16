from django.conf import settings
from django.db.models import Q

DEFAULT_SETTINGS = {
    'RELATION_MODELS': [],
    'ACTIVITY_FIELDS': [],
    'LESSON_FIELDS': [],
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
    'JAVASCRIPT_URL': settings.MEDIA_URL + 'js/',
    'CREDIT_MODEL': None,
}

DEFAULT_SETTINGS.update(getattr(settings, 'LESSON_SETTINGS', {}))

globals().update(DEFAULT_SETTINGS)

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]
