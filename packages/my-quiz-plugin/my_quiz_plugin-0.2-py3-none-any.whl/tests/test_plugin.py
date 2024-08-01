import os
import sys
import unittest
from bs4 import BeautifulSoup
from mkdocs.config import Config, config_options
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_quiz_plugin.plugin import QuizPlugin

class TestQuizPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = QuizPlugin()
        self.plugin.config = {
            'quiz_file': os.path.join(os.path.dirname(__file__), '..', 'quizzes.json'),
            'language': 'en'
        }
        self.mock_schema = (
            ('site_name', config_options.Type(str, default='My Docs')),
            ('site_url', config_options.Type(str, default='')),
            ('repo_url', config_options.Type(str, default='')),
            ('site_author', config_options.Type(str, default='')),
            ('site_description', config_options.Type(str, default='')),
        )
        self.config = Config(self.mock_schema)
        self.config.load_dict(self.plugin.config)
        self.plugin.on_config(self.config)

    def test_load_quiz_data(self):
        self.assertIn('quizzes', self.plugin.quiz_data)
        self.assertIn('quiz1', self.plugin.quiz_data['quizzes'])
        self.assertIn('quiz2', self.plugin.quiz_data['quizzes'])

    def test_generate_quiz_html(self):
        quiz = self.plugin.quiz_data['quizzes']['quiz1']
        quiz_html = self.plugin.generate_quiz_html(quiz)
        print(quiz_html)  # Debugging: Print the generated HTML

        soup = BeautifulSoup(quiz_html, 'html.parser')
        self.assertTrue(soup.find(string='What is the capital of France?'))

        # Check the presence of options in the quiz
        options = [li.get_text(strip=True) for li in soup.find_all('li')]
        self.assertIn('Berlin', options)
        self.assertIn('Madrid', options)
        self.assertIn('Paris', options)
        self.assertIn('Rome', options)

        # Check the presence of indices
        indices = [li['data-indice'] for li in soup.find_all('li')]
        self.assertIn('This is the capital of Germany.', indices)
        self.assertIn('This is the capital of Spain.', indices)
        self.assertIn('', indices)
        self.assertIn('This is the capital of Italy.', indices)

    def test_on_page_markdown(self):
        markdown = """
        # Sample Page

        <!-- QUIZ_ID: quiz1 -->
        """
        file = File('sample_page.md', 'docs', 'site', False)
        page = Page('Sample Page', file, self.config)
        updated_markdown = self.plugin.on_page_markdown(markdown, page, self.config, None)
        print(updated_markdown)  # Debugging: Print the updated markdown

        soup = BeautifulSoup(updated_markdown, 'html.parser')
        self.assertTrue(soup.find(string='What is the capital of France?'))

        # Check the presence of options in the quiz
        options = [li.get_text(strip=True) for li in soup.find_all('li')]
        self.assertIn('Berlin', options)
        self.assertIn('Madrid', options)
        self.assertIn('Paris', options)
        self.assertIn('Rome', options)

    def test_hint_functionality(self):
        quiz = self.plugin.quiz_data['quizzes']['quiz1']
        quiz_html = self.plugin.generate_quiz_html(quiz)
        print(quiz_html)  # Debugging: Print the generated HTML

        soup = BeautifulSoup(quiz_html, 'html.parser')

        # Check the presence of indices
        indices = [li['data-indice'] for li in soup.find_all('li')]
        self.assertIn('This is the capital of Germany.', indices)
        self.assertIn('This is the capital of Spain.', indices)
        self.assertIn('This is the capital of Italy.', indices)

    def test_show_correct_answer(self):
        quiz = self.plugin.quiz_data['quizzes']['quiz1']
        quiz_html = self.plugin.generate_quiz_html(quiz)
        print(quiz_html)  # Debugging: Print the generated HTML

        soup = BeautifulSoup(quiz_html, 'html.parser')

        # Check for the presence of correct and incorrect classes
        self.assertTrue(soup.find(class_='correct'))
        self.assertTrue(soup.find(class_='incorrect'))

if __name__ == '__main__':
    unittest.main()

