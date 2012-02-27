from lessons.models import *
from edumetadata.models import Grade, Subject

def init_data():
    grades = [Grade.objects.get(slug=x) for x in ['6', '7', '8']]

    p = PhysicalSpaceType(name='Classroom')
    p.save()

    for grouping_type in ['Cross-age teaching', 'Heterogeneous grouping', 'Homogeneous grouping', 'Individualized instruction', 'Jigsaw grouping', 'Large-group instruction', 'Multi-level instruction', 'Non-graded instructional grouping', 'One-to-one tutoring', 'Small-group instruction']:
        g = GroupingType(name=grouping_type)
        g.save()

    for material in [u'Atlas', u'Beaker', u'Calculators', u'Chalk', u'Clay', u'Compasses', u'Crayons', u'Erasers', u'Globe', u'Glue', u'Highlighters', u'Magazines', u'Magnets', u'Markers', u'Microscopes', u'Newspapers', u'Paper', u'Pencils', u'Pens', u'Protractor', u'Rulers', u'Safety goggles', u'Scissors', u'String', u'Thermometers', u'Apple peels', u'Black construction paper', u'Black paint', u'Bunson burner', u'Chart paper', u'Cheesecloth', u'Clipboards', u'Colored paper', u'Colored pencils', u'Completed worksheets from previous activity', u'Construction paper', u'Drawing paper', u'Dry erase markers', u'Field guides', u'Fine mesh', u'Fishing line', u'Food coloring', u'Grass clippings', u'Index cards', u'Latex gloves', u'Leaves', u'Lined or ruled paper', u'Meter sticks', u'Modeling clay', u'Paint', u'Paintbrushes', u'Paper clips', u'Petri dish', u'Pipe cleaners', u'Plastic containers', u"Rope (6-8')", u'Rubber bands', u'Rubber dishwashing gloves', u'Safety scissors', u'Shoe boxes with lids', u'Species keys', u'Sticky notes', u'Stopwatch', u'String (several different colors)', u'Two-liter plastic bottles', u'Vegetable shortening', u'Wall map of the world', u'Water', u'Writing paper', u'Watercolors', u'Transparent tape', u'2-liter plastic bottles, tops and bottoms cut off', u'Scale', u'Bucket', u'Ice water', u'Thumbtacks', u'A small, solid object such as a shell, coin, key', u'Stir sticks', u'Photo of your school', u'Plaster of Paris', u'Toothpicks', u'Sponge', u'Labels', u'Notebooks', u'Photographs of a place in your community', u'Yarn', u'Stapler', u'Binoculars', u'National weather map from the local newspaper', u'Backpack', u'Items that might be found in a backpack', u'Cork', u'Large pan', u'Contour maps of your local area', u'Tape measure', u'Art paper', u'Push pins', u'Removable adhesive dots', u'Graph paper', u'Large container for collecting trash', u'Large calendar', u'Gardening trowels', u'Magnifying glasses', u'Pasta in assorted shapes', u'Waxed paper', u'Blue enamel paint', u'Tempera paint', u'A miniature item, such as a toy car', u'Plastic or metal trays', u'Blank transparencies', u'Edible baking ingredients', u'Edible snack foods', u'Wall map of the United States', u'Spoons', u'Clear cups or bowls', u'Vegetable oil', u'Hula hoop', u'Posterboard', u'Balls of clay (3" in diameter)', u'Maps of a shopping mall', u'Photographs of your neighborhood, town, or state', u'Historical documents about your community', u'Glue sticks', u'State weather maps from the local newspaper', u'Photos of weather from magazines', u'Paper tablecloths', u'Encyclopedias (online access or hard copies)', u'The Very Hungry Caterpillar by Eric Carle', u'Several sheets of blank paper per student', u'Blindfolds', u'1 small, soft ball', u'Student journals', u'Large plastic garbage bags', u'Baseball cap', u'Centimeter tape measure', u'Example of haiku poetry', u'They Swim the Seas by Seymour Simon', u'Unifix Cube', u'Measuring Tape', u'Colored Markers', u'Garbage bags', u'Recycling container', u'Giant sticky notes', u'Large bulletin board', u'Colored thread', u'Fish-shaped pretzels ', u'Fish-shaped crackers ', u'One medium-sized bowl per group', u'Butcher paper', u'Removable tape or glue', u'Calendar', u'Flashlights', u'Polystyrene foam balls or round fruit', u'8-inch or 9-inch pie tins', u'Spoons or stirrers', u'Glass pie plate', u'Cornstarch', u'Meter sticks or rulers', u'Aluminum foil', u'Sewing needles or push pins', u'Shoeboxes, or 2-foot rectangular cardboard boxes', u'Telescope or binoculars', u'White paper', u'White poster board', u'Clear packing tape', u'Quart-sized glass jars with lids', u'2-liter plastic soda bottles', u'Laser pointer or gooseneck lamp', u'Low-melt glue or superglue', u'Plastic straws', u'Sand', u'Small bar magnets (not refrigerator magnets)', u'Small craft mirrors', u'Thread', u'2-liter bottle preforms (optional)', u'Bar or earth magnets', u'Fine metal filings or magnetic laser printer toner', u'Magnetic compasses', u'Mineral oil', u'Paper towels', u'Plastic petri dishes', u'Sealable plastic sandwich bags', u'Stirrers', u'Tablespoons or graduated cylinders', u'2 pieces of stiff, white cardboard', u'Colored construction paper', u'Duct tape or other strong tape', u'Hole puncher', u'Paper towel or wrapping paper tubes', u'2 Cups of water', u'2 Cups of dry ice (frozen carbon dioxide)', u'2 spoonfuls of sand or dirt', u'Dash of dark corn syrup or other organic material', u'Dash of ammonia', u'Large, plastic mixing bowl', u'4 medium-sized plastic garbage bags', u'Work gloves', u'Hammer', u'Large mixing spoon', u'Bubble wrap', u'Egg cartons, cut up into sections', u'Paper cups', u'Plastic garbage bags', u'Raw eggs (5 per small group)', u'Stepladder', u'Styrofoam', u'Tarp or large sheet of plastic', u'Timer or stopwatch', u'Drop cloth', u'Hand mirrors', u'Hats', u'Ball of string', u'World atlas', u"Groups' completed worksheets from Lesson 1, Act. 1", u'Completed worksheets from Lesson 1, Activity 1', u'Blank paper', u'Map transparencies', u'Reading passage from Lesson 3, Activity 1', u'White card stock', u'White card stock or construction paper', u'Completed worksheets from Lesson 5, Activity 2', u'Notes from Lesson 2, Activity 2 of this unit']:
        m = Material(name=material)
        m.save()

    for teaching_method_type in ['Brainstorming', 'Cooperative learning', 'Demonstrations', 'Discovery learning', 'Discussions', 'Drill', 'Experiential learning', 'Guided Listening', 'Hands-on learning', 'Information organization', 'Inquiry', 'Jigsaw', 'Lab procedures', 'Lecture', 'Modeling', 'Multimedia instruction', 'Peer tutoring', 'Programmed instruction', 'Reading', 'Reflection', 'Research', 'Role playing', 'Self-directed learning', 'Self-paced learning', 'Simulations and games', 'Visual instruction', 'Writing']:
        tmt = TeachingMethodType(name=teaching_method_type)
        tmt.save()
    for tst in [u'1 computer per classroom', u'1 computer per learner', u'1 computer per small group', u'Audio recording device', u'DVD player', u'Digital camera (and related equipment)', u'GPS units', u'Interactive whiteboard', u'Media production software', u'Microphone', u'Mobile data device (mobile phone, PDAs)', u'Mobile media player (MP3 player)', u'Presentation software', u'Printer', u'Projector', u'Scanner', u'Speakers', u'Television', u'VCR', u'Video camera (and related equipment)', u'Webcam', u'Word processing software']
        tst = TechSetupType(title=tst)
        tst.save()
    for name, url in {('Active X', 'http://www.activexguide.com/new/downloads.php'),
                      ('Flash', 'http://get.adobe.com/flashplayer/'),
                      ('Microsoft Silverlight', 'http://www.microsoft.com/silverlight/'),
                      ('Quicktime', 'http://www.apple.com/quicktime/'),
                      ('Real Player', 'http://www.real.com/'),
                      ('Shockwave', 'http://get.adobe.com/shockwave/')}:
        pt = PluginType(name=name, source_url=url)
        pt.save()

    a = Activity(title='Drawing Political Borders', id_number=418)
    a.slug ='drawing-political-borders'
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
    a.save()
    a.teaching_method_types = []
    for teaching_method in ['Brainstorming', 'Cooperative learning', 'Discovery learning', 'Discussions', 'Hands-on learning']:
        tmt = TeachingMethodType.objects.get(name=teaching_method)
        a.teaching_method_types.add(tmt)
    a.grouping_types = []
    for grouping_type in ['Heterogeneous grouping', 'Large-group instruction', 'Small-group instruction']:
        gt = GroupingType.objects.get(name=grouping_type)
        a.grouping_types.add(gt)
    a.grades = grades
    a.tech_setup_types = []
    for tech_setup_type in ['1 computer per classroom', 'Projector']:
        tst = TechSetupType.objects.get(title=tech_setup_type)
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
        m = Material.objects.get(name=material)
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

    a2 = Activity(title='Comparing Political Borders', id_number=419)
    a2.slug ='comparing-political-borders'
    a2.pedagogical_purpose_type = 2
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
    a2.duration = 50
    a2.internet_access_type = 'no'
    a2.teaching_approach_type = 'for-use'
    a2.save()
    a2.teaching_method_types = []
    for teaching_method in ['Brainstorming','Discussions', 'Reflection']:
        tmt = TeachingMethodType.objects.get(name=teaching_method)
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
        m = Material.objects.get(name=material)
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
