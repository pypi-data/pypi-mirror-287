from setuptools import setup, find_packages

setup(
    name='asrch',
    version='7.8.0',
    author='j',
    author_email='none@none.com',
    description='A terminal based webscraper + web browser.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://bitbucket.org/asrch/asrchpublic/src/main/',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
