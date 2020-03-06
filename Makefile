serve:
	flask run
po:
	pybabel extract -F translations/babel.cfg -k lazy_gettext -o translations/messages.pot .

init_lang:
	pybabel init -i translations/messages.pot -d translations -l $(lang)

compile:
	pybabel compile -d translations
