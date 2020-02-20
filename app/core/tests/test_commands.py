from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db wehn db is available"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True  # Override ConnectionHandler to return true
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # Mock test to pretend that you are waiting
    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)