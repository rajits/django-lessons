from lessons.models import *
from edumetadata.models import Grade, Subject

def init_data():
    grades = [Grade.objects.get(slug=x) for x in ['6', '7', '8']]

    p = PhysicalSpaceType(name='Classroom')
    p.save()

    a = Activity(title='Drawing Political Borders')
    a.slug ='drawing-political-borders'
    a.id_number = 418
    a.pedagogical_purpose_type = 2
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
    a.duration = 50
    a.internet_access_type = 'optional'
    a.teaching_approach_type = 'for-use'
    a.teaching_methods = ['brainstorming', 'cooperative', 'discovery','discussions', 'hands-on']
    a.grouping_types = ['heterogeneous', 'large-group', 'small-group']
    a.save()
    a.grades = grades
    a.tech_setup_types = []
    for tech_setup_type in ['1 computer per classroom', 'Projector']:
        tst = TechSetupType(title=tech_setup_type)
        tst.save()
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
        s = Subject(name=subject)
        s.save()
        a.subjects.add(s)
    a.materials = []
    for material in ['Colored pencils', 'Pencils', 'Pens', 'Sticky notes']:
        m = Material(name=material)
        m.save()
        a.materials.add(m)
    a.physical_space_type = [p]
    a.standards = []
    for name in ['National Geography Standards: Standard 1',
                 'National Geography Standards: Standard 5',
                 'National Geography Standards: Standard 13',
                 'National Council for Social Studies Curriculum Standards: Theme 3']:
        s = Standard(name=name)
        s.save()
        a.standards.add(s)
    a.save()

    l = Lesson(title='Political Borders', slug='political-borders')
    l.subtitle_guiding_question = 'Why are the borders of countries located in certain places?'
    l.description = '''Students think about regions and borders by determining where they would place borders in 
                    an artificial continent, based on a set of physical and cultural features of the area.'''
    l.duration = 100
    # instance needs a pk before a m2m relationship can be used
    l.save()
    l.grades = grades
    l.save()
