from lessons.models import *
from edumetadata.models import Grade, Subject

def init_data():
    grades = [Grade.objects.get(slug=x) for x in ['6', '7', '8']]

    p, created = PhysicalSpaceType.objects.get_or_create(name='Classroom')

    a, created = Activity.objects.get_or_create(title='Drawing Political Borders',
                                                id_number=418,
                                                slug='drawing-political-borders',
                                                pedagogical_purpose_type=2,
                                                duration=50)
    if created:
        a.description = '''Students examine maps that show physical and cultural features of a fictitious area. Students draw borders based on how they think the land 
                        should be divided.'''
        a.subtitle_guiding_question = '''<!-- SANITIZE EXEMPT --><!-- SANITIZE EXEMPT -->
                                      <p>How are regions defined? How are land and resources divided <br />among countries?</p>'''
        a.learning_objectives = '''<!-- SANITIZE EXEMPT --><p>Students will be able to:</p>
                                <ul>
                                <li>consider how physical and cultural features could be used to define country borders </li>
                                <li>discuss their ideas about which features are most important in establishing good borders</li>
                                </ul>'''
        a.background_information = '''<!-- SANITIZE EXEMPT --><p>Maps can be used as tools to help us understand our world. Specifically, 
                                   maps can help demonstrate how borders intersect physical and human geographical features, and how 
                                   those intersections can lead to cooperation and/or conflict. Borders of regions or of countries define an 
                                   area, which has a particular shape and size. Sometimes physical features define the border of a region or 
                                   a country. For example, coastlines are borders between the regions of land and water, and mountains 
                                   may serve as borders between different countries or different cultural groups. Country borders, however 
                                   determined, define a physical space over which a country exercises control. When a political border is 
                                   imposed on the physical landscape, it defines the area, shape, and size of the country, as well as the 
                                   physical features and natural resources available. These factors of shape and size can influence the ways 
                                   in which human activity is structured; for example, land use, transportation, and settlement patterns. 
                                   Sometimes the shape and size suggest that a country may want to expand its borders in order to 
                                   increase its size, change its shape, and/or control more resources.</p>'''
        a.prior_knowledge = '<!-- SANITIZE EXEMPT --><ul><li>None</li></ul>'
        a.other_notes = '''<!-- SANITIZE EXEMPT --><p>Optional: Before starting the activity, increase the size and make 
                        full-sized transparencies of the four maps on the worksheet Draw  Political Borders, by printing the 
                        images on transparency paper.</p>'''
      # a.directions = '''<!-- SANITIZE EXEMPT --><p><strong>1. Activate students' prior knowledge and introduce vocabulary. </strong></p>'''
        a.assessment_type = 'informal'
        a.assessment = '''<!-- SANITIZE EXEMPT --><p>During the small group discussions, ask students to explain their 
                       understanding of borders and regions, and their reasons for creating borders where they did on their 
                       maps. Encourage students to use the information in the Religions, Mountains and Rivers, and Languages 
                       maps in their explanations.</p>'''
        a.internet_access_type = 'optional'
        a.teaching_approach_type = 'for-use'
        a.save()
        a.teaching_method_types = []
        for teaching_method in ['Brainstorming', 'Cooperative learning', 'Discovery learning', 'Discussions', 'Hands-on learning']:
            tmt, created = TeachingMethodType.objects.get_or_create(name=teaching_method)
            a.teaching_method_types.add(tmt)
        a.grouping_types = []
        for grouping_type in ['Heterogeneous grouping', 'Large-group instruction', 'Small-group instruction']:
            gt, created = GroupingType.objects.get_or_create(name=grouping_type)
            a.grouping_types.add(gt)
        a.grades = grades
        a.tech_setup_types = []
        for tech_setup_type in ['1 computer per classroom', 'Projector']:
            tst, created = TechSetupType.objects.get_or_create(title=tech_setup_type)
            a.tech_setup_types.add(tst)
        a.tips = []
        for tip in ['Print the worksheet Draw Political Borders on transparency paper. Cut the transparency into quarters',
                  'You may want to start the activity by first making a connection to your ...']:
            t = Tip(body=tip, tip_type=1)
            t.save()
            a.tips.add(t)
        a.skills = []
        for skill in ['Critical Thinking Skills: Understanding',
                    'Critical Thinking Skills: Applying',
                    'Critical Thinking Skills: Analyzing',
                    'Critical Thinking Skills: Creating',
                    '21st Century Skills: Learning and Innovation Skills: Communication and Collaboration',
                    '21st Century Skills: Learning and Innovation Skills: Creativity and Innovation',
                    '21st Century Skills: Life and Career Skills: Social and Cross-Cultural Skills',
                    'Geographic Skills: Analyzing Geographic Information',
                    'Geographic Skills: Organizing Geographic Information',
                    'Geographic Skills: Asking Geographic Questions',
                    'Geographic Skills: Answering Geographic Questions',
                    'NETS*S: Communication and Collaboration',
                    'NETS*S: Creativity and Innovation']:
            s = Skill(name=skill)
            s.save()
            a.skills.add(s)
        a.subjects = []
        for subject in ['Geography: Human Geography', 'Geography: Physical Geography',
                      'Social Studies: Human behavior', 'Social Studies: Human relations']:
            s, created = Subject.objects.get_or_create(name=subject)
            a.subjects.add(s)
        a.materials = []
        for material in ['Colored pencils', 'Pencils', 'Pens', 'Sticky notes']:
            m, created = Material.objects.get_or_create(name=material)
            a.materials.add(m)
        a.physical_space_types.add(p)
        a.standards = []
        for name in ['National Geography Standards: Standard 1',
                     'National Geography Standards: Standard 5',
                     'National Geography Standards: Standard 13',
                     'National Council for Social Studies Curriculum Standards: Theme 3']:
            s = Standard(name=name)
            s.save()
            a.standards.add(s)
        a.save()

    a2, created = Activity.objects.get_or_create(title='Comparing Political Borders',
                                                 id_number=419,
                                                 slug='comparing-political-borders',
                                                 pedagogical_purpose_type=2,
                                                 duration=50)
    if created:
        a2.description = '''<!-- SANITIZE EXEMPT --><p>Students compare their border selections based on physical and cultural 
                         features. They discuss other factors that could impact where borders are established.</p>'''
        a2.subtitle_guiding_question = '''<!-- SANITIZE EXEMPT --><p>What factors impact where borders are established?</p>'''
        a2.learning_objectives = '''<!-- SANITIZE EXEMPT --><p>Students will be able to:</p>
                                <ul>
                                <li>explain and compare their border selections based on physical and cultural features </li>
                                <li>discuss other factors that could impact where borders are established</li>
                                </ul>'''
        a2.background_information = '''<!-- SANITIZE EXEMPT --><p>Maps can be used as tools to help us understand our world. Specifically, 
                                    maps can help demonstrate how borders intersect physical and human geographical features, and how 
                                    those intersections can lead to cooperation and/or conflict. Borders of regions or of countries define an 
                                    area, which has a particular shape and size. Sometimes physical features define the border of a region or 
                                    a country. For example, coastlines are borders between the regions of land and water, and mountains 
                                    may serve as borders between different countries or different cultural groups. Country borders, however 
                                    determined, define a physical space over which a country exercises control. When a political border is 
                                    imposed on the physical landscape, it defines the area, shape, and size of the country, as well as the 
                                    physical features and natural resources available. These factors of shape and size can influence the ways 
                                    in which human activity is structured; for example, land use, transportation, and settlement patterns. 
                                    Sometimes the shape and size suggest that a country may want to expand its borders in order to 
                                    increase its size, change its shape, and/or control more resources.</p>'''
        a2.prior_knowledge = '<!-- SANITIZE EXEMPT --><ul><li>None</li></ul>'
      # a.directions = '''<!-- SANITIZE EXEMPT --><p><strong>1. Activate students' prior knowledge and introduce vocabulary. </strong></p>'''
        a2.assessment_type = 'informal'
        a2.assessment = '''<!-- SANITIZE EXEMPT --><p>Evaluate students based on their participation in the whole-class 
                        discussion.</p>'''
        a2.internet_access_type = 'no'
        a2.teaching_approach_type = 'for-use'
        a2.save()
        a2.teaching_method_types = []
        for teaching_method in ['Brainstorming','Discussions', 'Reflection']:
            tmt, created = TeachingMethodType.objects.get_or_create(name=teaching_method)
            a2.teaching_method_types.add(tmt)
        a2.grouping_types = [GroupingType.objects.get(name='Large-group instruction')]
        a2.grades = grades
        a2.skills = []
        for skill in ['Critical Thinking Skills: Understanding',
                    'Critical Thinking Skills: Analyzing',
                    'Critical Thinking Skills: Evaluating',
                    'Geographic Skills: Analyzing Geographic Information',
                    'Geographic Skills: Asking Geographic Questions',
                    'Geographic Skills: Answering Geographic Questions']:
            s, created = Skill.objects.get_or_create(name=skill)
            a2.skills.add(s)
        a2.subjects = []
        for subject in ['Geography: Human Geography', 'Geography: Physical Geography',
                      'Social Studies: Human behavior', 'Social Studies: Human relations']:
            s, created = Subject.objects.get_or_create(name=subject)
            a2.subjects.add(s)
        a2.materials = []
        for material in ['Pencils', 'Pens', 'Lined or ruled paper', 'Completed worksheets from Lesson 1, Activity 1']:
            m, created = Material.objects.get_or_create(name=material)
            a2.materials.add(m)
        a2.physical_space_types.add(p)
        a2.standards = []
        for name in ['National Geography Standards: Standard 1',
                     'National Geography Standards: Standard 5',
                     'National Geography Standards: Standard 13',
                     'National Council for Social Studies Curriculum Standards: Theme 3']:
            s = Standard(name=name)
            s.save()
            a2.standards.add(s)
        a2.save()

    l = Lesson(title='Political Borders', slug='political-borders')
    l.subtitle_guiding_question = 'Why are the borders of countries located in certain places?'
    l.description = '''Students think about regions and borders by determining where they would place borders in 
                    an artificial continent, based on a set of physical and cultural features of the area.'''
    l.duration = 100
    l.other_notes = 'This is lesson 1 in a series of 10 lessons in a unit on Europe.'
    # instance needs a pk before a m2m relationship can be used
    l.save()
    l.grades = grades
    l.save()

    lr = LessonActivity(lesson=l, activity=a)
    lr.transition_text = "Make sure you have groups' completed maps from Lesson 1, Activity 1 in the Beyond Borders unit"
    lr.save()

    lr2 = LessonActivity(lesson=l, activity=a2)
    lr2.save()
