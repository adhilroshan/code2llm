import unittest
from click.testing import CliRunner
from app import start  # Import the start command from your app module

class ClickCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_start_command_valid(self):
        result = self.runner.invoke(start, ['--directory', '.', '--max-chars', '3000', '--port', '2277'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Code2LLM server', result.output)

    def test_start_command_missing_directory(self):
        result = self.runner.invoke(start, ['--max-chars', '3000', '--port', '2277'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error: Missing option "--directory"', result.output)

    def test_start_command_invalid_port(self):
        result = self.runner.invoke(start, ['--directory', '.', '--max-chars', '3000', '--port', 'invalid'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error: Invalid value for "--port"', result.output)

if __name__ == '__main__':
    unittest.main()