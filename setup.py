from setuptools import setup

version = '0.1.dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
#    open('CHANGES.rst').read(),
    ])

install_requires = [
    'flask',
    'flask-bootstrap',
    'numpy',
    'PIL',
    'setuptools',
    ],

tests_require = [
    ]

setup(name='crumble',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='TODO',
      author_email='info@technokrat.nl',
      url='',
      license='BSD',
      packages=['crumble'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
              'runserver = crumble.main:go',
          ]},
      )
