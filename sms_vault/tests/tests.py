import unittest
import transaction

from pyramid import testing
from ..models import db, User, Base
from . import TestBase, FunctionalTestBase

import logging
log = logging.getLogger(__name__)

class TestSite(TestBase):
    "Unit and Integration tests"

    def test_record_add(self):
        with transaction.manager:
            record = User(user_id=u'testuser', password=u'testpass')
            db.add(record)

    def test_record_fetch(self):
        user = db.query(User).first()
        self.assertIsNotNone(user)
        self.assertEquals(user.user_id, u'testuser')

    def test_homepage(self):
        from ..controllers.controllers import homepage

        request = testing.DummyRequest()
        request.session['logged_in_user'] = 'admin'
        response = homepage(request)
        log.info(response)

        assert 'msg_counts' in response


class TestSiteFunctional(FunctionalTestBase):
    "Functional tests for the project"

    def test_get_login(self):
        res = self.app.get('/login')
        self.assertEqual(res.status_int, 200)

