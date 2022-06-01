from predict import final_result
from predict import run_LR
from predict import run_RF
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual(final_result('data','data'),"/data/allinfo_XGBoost_info.csv")
        self.assertEqual(run_RF('data','data'),"/data/submission_RF.csv")
        self.assertEqual(run_LR('data','data'),"/data/submission_LR.csv")
if __name__=="__main__":
    unittest.main()