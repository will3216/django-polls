import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any patch
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name = 'django-polls',
  version = '0.1',
  packages = ['polls'],
  include_package_data = True,
  license = 'BSD License',
  description = 'A simple Django app to conduct Web-based polls.',
  long_description = README,
  url = '',
  author = 'William Bryant',
  author_email = 'willtbryant@gmail.com',
  classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License', 
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  ],
)
