import pytest
import os
import sys
import json

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from app_faker import app


def test_delete_records():
    print("Get data faker")
    resp = app.test_client().get("datos")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert len(res.get("datos")) == 13
