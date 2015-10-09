import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        result = self.client.get("/")
        self.assertIn("Please RSVP", result.data)
        self.assertNotIn("Party Details", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        # FIXME: check that once we log in, we see party details -- and don't see form!
        self.assertNotIn("Please RSVP", result.data)
        self.assertIn("Party Details", result.data)

    def test_rsvp_mel(self):
        # FIXME: write a test that mel can't invite himself
        result = self.client.post("/rsvp",
                                  data={'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"},
                                  follow_redirects=True)
        # FIXME: check that once we log in, we see party details -- and don't see form!
        self.assertNotIn("Party Details", result.data)

if __name__ == "__main__":
    unittest.main()