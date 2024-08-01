from setuptools import setup, find_packages

setup(
    name='my_quiz_plugin',
    version='0.1',
    description='A MkDocs plugin to create quizzes',
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
    }
)

