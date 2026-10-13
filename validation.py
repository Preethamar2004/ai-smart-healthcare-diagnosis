
def validate_patient_age(age):
    """Check whether the age is a valid integer."""
    return type(age) is int and 0 <= age <= 120


def validate_patient_id(patient_id):
    """Check whether the patient ID is non-empty."""
    return (
        isinstance(patient_id, str)
        and bool(patient_id.strip())
    )
