import lib.core as core

def test_guard():
    assert core.deltaM113_guard(0.5) == "rollback triggered"
    assert core.deltaM113_guard(0.9) == "stable"

def test_zdm():
    d = core.zdm_dual_memory("zoran")
    assert d["persistent"] == "zoran"
    assert d["resonant"] == "naroz"
