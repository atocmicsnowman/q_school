"""
utilities for registration views
"""
from q_school.settings import REQUIRED_USER_UPLOAD_CSV_FIELDS

def validate_users_upload_formatted(header_row: set):
    """
    Ensure that required headers are available
    """    
    return header_row & REQUIRED_USER_UPLOAD_CSV_FIELDS == REQUIRED_USER_UPLOAD_CSV_FIELDS
