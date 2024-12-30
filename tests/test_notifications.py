import unittest
from logic.notifications import send_error_notification

class TestNotifications(unittest.TestCase):
    def test_send_error_notification(self):
        # This is a dummy test invocation
        send_error_notification("Dummy error message for testing purposes.")

if __name__ == "__main__":
    unittest.main()