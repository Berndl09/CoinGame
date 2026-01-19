import pytest
import json
from coin_collector.config import load_level

def test_invalid_level_type(tmp_path):
    bad_data = {"width": "Viel zu breit", "coins": []}
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(bad_data))
    
    with pytest.raises(Exception):
        load_level(str(p))