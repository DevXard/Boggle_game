from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Redy to play Boggle?</h1>', html)
    
    def test_game_board(self):
        with self.client as client:
            with client.session_transaction() as session:
                session['board'] = [['C','A','T','T','T'],
                                    ['C','A','T','T','T'],
                                    ['C','A','T','T','T'],
                                    ['C','A','T','T','T'],
                                    ['C','A','T','T','T'],]
        res = self.client.get('/check-awncer?guess=cat')
        self.assertEqual(res.json['response'], 'ok')
