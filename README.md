# Flask-Babel
Can't get it to work...

Getting Started
===============
1. Install
`bash install.sh`

2. Run
`bash run.sh`

Translations
============
1. In Jinja2
`{{ _('Bonjour') }}`

2. In Python
 Use Babel's gettext: 

 `from flask.ext.babel import gettext`
 `gettext('Hello')`

3. Update translation files: `bash babel-update.sh`

4. Set translations in .po file: `translations/en/LC_MESSAGES/messages.po`

5. Compile translations: `bash babel-compile.sh`

6. Should see 'Hello' instead of 'Bonjour' but it doesn't happen.

Note
====
Getting the locale to translate has been hardced to english (i.e. "en").
The get_locales function fires as expected but translation doesn't actually occur
See \_\_init\_\_.py:

`@babel.localeselector`
`def get_locale():`
  `return 'en'`

We should be seeing "Hello" instead of "Bonjour".



