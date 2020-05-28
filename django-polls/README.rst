=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitor can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quict start

1. Add "polls" to your INSTALLE_APPS setting like this::

	INSTALLED_APPS = [
	'...'
	'polls',
	]

2. Include the polls URLconf in your project urls.py like this::

	url(r'^polls/', inlcude('polls.urls'))

3. Run `python manage.py migrate` to create polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ 
to create a poll (you'll need the Admin app enabled)

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll

