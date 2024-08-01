import re
import uuid
import json
from mkdocs.plugins import BasePlugin
import os
import warnings
from mkdocs.config import config_options

warnings.filterwarnings("ignore")

class QuizPlugin(BasePlugin):

    config_scheme = (
        ('quiz_file', config_options.Type(str, default='quizzes.json')),
        ('language', config_options.Type(str, default='en')),
    )

    def on_config(self, config):
        quiz_file_path = self.config.get('quiz_file')
        self.language = self.config.get('language', 'en')
        if quiz_file_path and os.path.isfile(quiz_file_path):
            try:
                with open(quiz_file_path, 'r') as file:
                    self.quiz_data = json.load(file)
                print("JSON is valid")
            except json.JSONDecodeError as e:
                print(f"JSON is invalid: {e}")
                self.quiz_data = {'quizzes': {}}
        else:
            self.quiz_data = {'quizzes': {}}
        return config

    def on_page_markdown(self, markdown, page, config, files):
        quiz_placeholder_pattern = re.compile(r'<!-- QUIZ_ID: (\w+) -->')
        matches = quiz_placeholder_pattern.findall(markdown)

        for quiz_id in matches:
            if quiz_id in self.quiz_data['quizzes']:
                quiz_html = self.generate_quiz_html(self.quiz_data['quizzes'][quiz_id])
                markdown = markdown.replace(f'<!-- QUIZ_ID: {quiz_id} -->', quiz_html)

        return markdown

    def generate_quiz_html(self, quiz):
        quiz_id = uuid.uuid4().hex
        questions = quiz.get('questions', [])
        quiz_html = f"<div class='quiz' id='quiz-{quiz_id}'>"

        for question in questions:
            question_id = uuid.uuid4().hex
            question_text = question['question'].get(self.language, question['question']['en'])
            quiz_type = question.get('type', 'multiple-choice')

            if quiz_type == 'multiple-choice' or quiz_type == 'true-false':
                options = question.get('options', [])
                quiz_html += f"""
                <div class='question p-4 border border-gray-200 rounded-lg shadow-md mb-6' id='question-{question_id}' data-quiz-id='{quiz_id}' data-question-id='{question_id}' data-quiz-type='{quiz_type}'>
                    <p class='font-bold text-lg mb-4'>{question_text}</p>
                    <ul class='list-none p-0'>
                """
                for i, option in enumerate(options):
                    text = option['text'].get(self.language, option['text']['en'])
                    indice = option.get('indice', {}).get(self.language, option.get('indice', {}).get('en', ''))
                    correct = 'correct' if option['correct'] else 'incorrect'
                    quiz_html += f"""
                        <li class='{correct} p-2 mb-2 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100' data-quiz-id='{quiz_id}' data-question-id='{question_id}' data-option-id='{i}' data-indice='{indice}'>
                            {text}
                        </li>
                    """
                quiz_html += f"""
                    </ul>
                    <div class='indice mt-4 p-3 border border-yellow-300 bg-yellow-100 text-yellow-700 rounded-lg hidden' id='indice-{question_id}'></div>
                    <div class='feedback mt-4 p-3 rounded-lg hidden' id='feedback-{question_id}'></div>
                </div>
                """
            elif quiz_type == 'fill-in-the-blank':
                answer = question['answer'].get(self.language, question['answer']['en'])
                indice = question.get('indice', {}).get(self.language, question.get('indice', {}).get('en', ''))
                quiz_html += f"""
                <div class='question p-4 border border-gray-200 rounded-lg shadow-md mb-6' id='question-{question_id}' data-quiz-id='{quiz_id}' data-question-id='{question_id}' data-quiz-type='{quiz_type}' data-answer='{answer}'>
                    <p class='font-bold text-lg mb-4'>{question_text}</p>
                    <input type='text' class='p-2 mb-2 border border-gray-200 rounded-lg' id='answer-{question_id}'>
                    <button class='submit-answer bg-blue-500 text-white p-2 rounded-lg' data-quiz-id='{quiz_id}' data-question-id='{question_id}'>Submit</button>
                    <div class='indice mt-4 p-3 border border-yellow-300 bg-yellow-100 text-yellow-700 rounded-lg hidden' id='indice-{question_id}'>{indice}</div>
                    <div class='feedback mt-4 p-3 rounded-lg hidden' id='feedback-{question_id}'></div>
                </div>
                """

        quiz_html += "</div>"
        return quiz_html