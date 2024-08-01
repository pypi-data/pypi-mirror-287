from setuptools import setup, find_packages
import os 

""" # Read the contents of the README file
def read_readme():
    with open(os.path.join(os.path.dirname(__file__), 'DOC_README.md'), encoding='utf-8') as f:
        return f.read()
"""    

setup(
    name='my_quiz_plugin',
    version='0.2',
    description='A MkDocs plugin to create quizzes',
    author_email='your.email@example.com',
    #long_description=read_readme(),
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.0.4',
        'beautifulsoup4>=4.11.1',
        'lxml>=4.9.1',
        'pytest>=7.4.4'
    ],
    entry_points={
        'mkdocs.plugins': [
            'my_quiz_plugin = my_quiz_plugin.plugin:QuizPlugin'
        ]
    },
    keywords='mkdocs plugin quizz',
    license='MIT',
    project_urls={
        'Bug Reports': 'https://github.com/bdllard/my_quiz_plugin/issues',
        'Source': 'https://github.com/bdallard/my_quiz_plugin',
    },

)

