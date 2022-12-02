import unittest

from party import app
from model import db, example_data, connect_to_db


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"board games, rainbows, and ice cream sundaes", result.data)

    def test_no_rsvp_yet(self):

        result = self.client.get("/") #setting result var to get the homepage data
        self.assertEqual(result.status_code, 200) #assertequal compares the first parameter with the second, makes sure the result returns a 200 code
        self.assertIn(b'<h2>Please RSVP</h2>', result.data) #assertIn checks if "Please RSVP" is in the result webpage. Serves as a 'panic button' if first param is not there

        #print("FIXME")

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={"name": "Jane",
                                        "email": "jane@jane.com"},
                                  follow_redirects=True)

        result_2 = self.client.get("/")
        self.assertEqual(result_2.status_code, 200)
        self.assertNotIn(b'<h2>Please RSVP</h2>', result_2.data)


        # print("FIXME")


class PartyTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database (uncomment when testing database)
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data (uncomment when testing database)
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        # (uncomment when testing database)
        db.session.close()
        db.drop_all()

    def test_games(self):
        # FIXME: test that the games page displays the game from example_data()
        result = self.client.get("/games") #result var assign 
        self.assertIn(b"<h2>Games</h2>", result.data)
        aquariangirl
        # print("FIXME")


if __name__ == "__main__":
    unittest.main()
