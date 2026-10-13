
import unittest
from validation import validate_patient_age, validate_patient_id


class TestPatientValidation(unittest.TestCase):
    def test_valid_age(self):
        self.assertTrue(validate_patient_age(45))

    def test_negative_age(self):
        self.assertFalse(validate_patient_age(-1))

    def test_invalid_age(self):
        self.assertFalse(validate_patient_age("45"))

    def test_valid_patient_id(self):
        self.assertTrue(validate_patient_id("PAT001"))

    def test_empty_patient_id(self):
        self.assertFalse(validate_patient_id(" "))


if __name__ == "__main__":
    unittest.main()
