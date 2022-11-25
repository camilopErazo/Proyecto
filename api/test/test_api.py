import pytest
import os
import sys
import json

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from api import app


def test_delete_all_records():
    print("Delete data faker")
    resp = app.test_client().get("eliminar_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert res.get("data") == "data eliminada"


def test_get_records():
    print("Get data faker")
    resp = app.test_client().get("registros_faker")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert len(res.get("data")) == 0


def test_create_records():
    print("Create data faker")
    resp = app.test_client().get("crear_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert res.get("data") == "Registros creados"
