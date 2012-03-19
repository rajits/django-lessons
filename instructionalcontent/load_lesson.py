from instructionalcontent.models import Activity, Lesson, LessonActivity

a, created = Activity.objects.get_or_create(slug='drawing-political-borders')
a2, created = Activity.objects.get_or_create(slug='comparing-political-borders')

l = Lesson(title='Political Borders', slug='political-borders', id_number='0417')
l.appropriate_for = 1
l.subtitle_guiding_question = 'Why are the borders of countries located in certain places?'
l.description = '''Students think about regions and borders by determining where they would place borders in 
                an artificial continent, based on a set of physical and cultural features of the area.'''
l.other_notes = 'This is lesson 1 in a series of 10 lessons in a unit on Europe.'
l.save()

lr = LessonActivity(lesson=l, activity=a)
lr.transition_text = "Make sure you have groups' completed maps from Lesson 1, Activity 1 in the Beyond Borders unit"
lr.save()

lr2 = LessonActivity(lesson=l, activity=a2)
lr2.save()
