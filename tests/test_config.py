from src.utils.config import GET_JDBC_PROPERTIES, COLUMN_RENAME_MAP

def test_get_jdbc_properties(monkeypatch):
    monkeypatch.setenv("PG_USER", "user")
    monkeypatch.setenv("PG_PASSWORD", "pass")

    props = GET_JDBC_PROPERTIES()
    assert props["user"] == "user"
    assert props["password"] == "pass"
    assert props["driver"] == "org.postgresql.Driver"

def test_column_rename_map_keys():
    mapa = COLUMN_RENAME_MAP()
    assert "VendorID" in mapa
    assert mapa["VendorID"] == "vendor_id"
