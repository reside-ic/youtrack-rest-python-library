from setuptools import setup

setup(
    name='YTClient',
    version='1.0.1',
    url='https://github.com/JoshLee0915/youtrack-rest-python-library',
    license='https://github.com/JoshLee0915/youtrack-rest-python-library/blob/master/LICENSE',
    author='Josh Lee',
    author_email='',
    description='A rewrite of the YouTrack python API',
    packages=['YTClient'],
    install_requires=['six>=1.12.0', 'httplib2>=0.12.1'],
    python_requires='>=3.6'
)
