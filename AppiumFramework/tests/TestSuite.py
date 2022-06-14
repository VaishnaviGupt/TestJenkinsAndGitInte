# Import the files
import unittest

from tests.LoginTests import LoginTests
from tests.ContactUsFormTest import ContactUsFormTest
from tests.EnterSomeValueTest import EnterValueTest
from tests.LongClickTest import LongClickTest
from tests.ScrollViewTest import ScrollViewTest

# Create the object of the class using unittest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactUsFormTest)
ev = unittest.TestLoader().loadTestsFromTestCase(EnterValueTest)
lg = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
lc = unittest.TestLoader().loadTestsFromTestCase(LongClickTest)
sv = unittest.TestLoader().loadTestsFromTestCase(ScrollViewTest)

# Create TestSuite
regressionTest = unittest.TestSuite([cf])

# Call the Test Runner Method
unittest.TextTestRunner(verbosity=1).run(regressionTest)




