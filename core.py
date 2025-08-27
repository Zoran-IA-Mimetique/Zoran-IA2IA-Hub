import json, hashlib, pathlib

REQUIRED = ["meta","hyperglottal","schemas","feeds","code","policies","injectors","docs","assets"]

def _stability_score(status: str) -> float:
    h = hashlib.sha256((";".join(sorted(REQUIRED))+status).encode()).hexdigest()
    return (int(h[:8], 16) % 1000)/1000.0

def delta_m11_3_guard(stability: float, threshold: float = 0.72) -> bool:
    """Return True if state is stable (no rollback), False otherwise."""
    return stability >= threshold

def hyperglottal_validate(zgs_path: str) -> bool:
    """Simple validation: file exists, balanced glyph chevrons, and contains ΔM11.3 tag."""
    p = pathlib.Path(zgs_path)
    if not p.exists():
        return False
    s = p.read_text(encoding="utf-8")
    return s.count("⟦") == s.count("⟧") and "ΔM11.3" in s

class ZoranHub:
    def __init__(self, repo_root="."):
        self.root = pathlib.Path(repo_root)

    def absorb(self) -> dict:
        missing = [d for d in REQUIRED if not (self.root/d).exists()]
        status = "ok" if not missing else "missing:" + ",".join(missing)
        stability = _stability_score(status)
        glyph_ok = hyperglottal_validate(str(self.root/"hyperglottal"/"zoran_core.zgs"))
        manifest_ok = (self.root/"feeds"/"zoran_manifest.json").exists()
        return {"status": status, "stability_score": stability, "glyph_valid": glyph_ok, "manifest_present": manifest_ok}
