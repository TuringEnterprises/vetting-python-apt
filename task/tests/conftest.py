import time

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    failed = 0
    passed = 0
    for failed_tests in terminalreporter.stats.get('failed', []):
      if 'hidden.py' in failed_tests.nodeid:
        failed = failed + 1

    for passed_tests in terminalreporter.stats.get('passed', []):
      if 'hidden.py' in passed_tests.nodeid:
        passed = passed + 1

    total = failed + passed
    print('total test cases:', total)
    print('passed test cases:', passed)
    print('failed test cases:', failed)

    duration = time.time() - terminalreporter._sessionstarttime
    print('duration:', duration, 'seconds')