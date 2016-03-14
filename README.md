<p align="center">
  <img src="https://avatars0.githubusercontent.com/u/1316274?v=3&s=200">
</p>

Foody - Django Sample Application
==================

This sample application demonstates how to setup, configure and use TML Django SDK in a web application. 

Before using this sample, please ensure you have a Translation Exchange account and you have created a sample application.


Installation
==================

Add the following dependency to your pom.xml:

```bash
$ virtualenv --no-site-packages foody_env
$ . ./foody_env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver localhost:8000
```

Configuration
==================

To be able to manage and translate the application yourself, you should create your own account on Translation Exchange, register a new application and use the application key in this sample. 

To update the application key, edit "foody/settings.py" file and replace YOUR_APPLICATION_KEY with the key from your application.

```python
TML = {
    'environment': 'dev',
    'application': {
       'key': 'YOUR_APPLICATION_KEY'
      },
    'monkeypatch': True,
    'cache': {
        'enabled': True,
        'adapter': 'memcached',
        'backend': 'pylibmc'
    },
    'data_preprocessors': ('tml.tools.list.preprocess_lists',),
    'env_generators': ('tml.tools.viewing_user.get_viewing_user',),
    'logger': {
        'path': pj(BASE_DIR, 'logs', 'tml.log')
    }
}
```

To learn more about all of the configuration options, please visit:

http://docs.translationexchange.com/django-quickstart/


Links
==================

* Register on TranslationExchange.com: http://translationexchange.com

* Follow TranslationExchange on Twitter: https://twitter.com/translationx

* Connect with TranslationExchange on Facebook: https://www.facebook.com/translationexchange

* If you have any questions or suggestions, contact us: support@translationexchange.com


Copyright and license
==================

Copyright (c) 2016 Translation Exchange, Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
