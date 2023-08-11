import pytest
from py_congress.bill import Bill
from py_congress.models.bill import *
from py_congress.config import generate_config
import json

def test_bill_client_create():
    config = generate_config()
    b = Bill(config)
    resp = b.get_bills(congress=116)
    print(resp)
    assert False
