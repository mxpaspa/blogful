import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful"
    DEBUG = True
    SECRET_KEY = os.environ.get("BLOGFUL_SECRET_KEY", os.urandom(12))
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"
    
class FilterTests(unittest.TestCase):
    def test_date_format(self):
        # Tonight we're gonna party...
        date = datetime.date(1999, 12, 31)
        formatted = dateformat(date, "%y/%m/%d")
        self.assertEqual(formatted, "99/12/31")

    def test_date_format_none(self):
        formatted = dateformat(None, "%y/%m/%d")
        self.assertEqual(formatted, None)