from multiprocessing import Pool
import unittest
from testAll import TestHome
from testAll import TestAbout

def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)

tests = [TestHome('test_TC001_py3_doc_button'),
        TestHome('test_TC002_blahblah_search'),
        TestHome('test_TC004_assert_title'),
        TestAbout('test_TC003_verify_upcoming_events_section_present'), 
        TestAbout('test_TC005_assert_url')]

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(run_test, tests)
