
import unittest
from django_alerts_cdn.alerts import bootstrap_alert, tailwind_alert

class TestAlerts(unittest.TestCase):

    def test_bootstrap_alert(self):
        result = bootstrap_alert("This is a test", "success")
        expected = '''
        <div class="alert alert-success" role="alert">
            This is a test
        </div>
        '''
        self.assertEqual(result.strip(), expected.strip())

    def test_tailwind_alert(self):
        result = tailwind_alert("This is a test", "success")
        expected = '''
        <div class="bg-green-500 text-white p-4 rounded-lg">
            This is a test
        </div>
        '''
        self.assertEqual(result.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
