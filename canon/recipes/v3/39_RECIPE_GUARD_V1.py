"""Standalone drift guard for the authorized author-recipe canon.

This verifies configuration identity, not backend correctness or execution authority.
No inference, GPU, network, or third-party dependencies.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import unittest

CANON_FILE = "39_CANON_RECETAS_AUTORES_Y_TALON_V3_20261125.json"
CANON_ID = "TALON_AUTHOR_RECIPES_CANON_V3_20261125"
CANON_SHA256 = "b061ace9598217014e5bf8b8fd85b67be4d4434531381dd00b8349578bc7d58d"


class RecipeDrift(ValueError):
    pass


def verify_bytes(raw):
    if hashlib.sha256(raw).hexdigest() != CANON_SHA256:
        raise RecipeDrift("Canon bytes differ from the published V3: explicit versioning required")
    data = json.loads(raw)
    if data["canon_id"] != CANON_ID:
        raise RecipeDrift("Wrong canon id")
    return data


def load_canon(path=None):
    return verify_bytes(Path(path or Path(__file__).with_name(CANON_FILE)).read_bytes())


def verify_effective_recipe(profile_id, effective, canon=None):
    canon = load_canon() if canon is None else canon
    if canon.get("canon_id") != CANON_ID:
        raise RecipeDrift("Wrong canon id")
    profile = canon["profiles"].get(profile_id)
    if profile is None or profile["comparison_recipe"] is None:
        raise RecipeDrift("Unknown or unadmitted recipe; no automatic fallback")
    expected = json.dumps(profile["comparison_recipe"], sort_keys=True, separators=(",", ":"), allow_nan=False)
    actual = json.dumps(effective, sort_keys=True, separators=(",", ":"), allow_nan=False)
    if actual != expected:
        raise RecipeDrift("Effective recipe drift: do not silently override the selected author recipe")
    return {"profile_id": profile_id, "canon_id": CANON_ID, "recipe_identity": "MATCH",
            "backend_validation": profile["admission"], "execution_authority": "NOT_GRANTED_BY_THIS_GUARD"}


class GuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canon = load_canon()

    def changed(self, name, field, value):
        recipe = copy.deepcopy(self.canon["profiles"][name]["comparison_recipe"])
        recipe[field] = value
        return recipe

    def test_all_ten_selected_recipes_match(self):
        valid = 0
        for name, profile in self.canon["profiles"].items():
            if profile["comparison_recipe"] is not None:
                self.assertEqual(verify_effective_recipe(name, profile["comparison_recipe"], self.canon)["recipe_identity"], "MATCH")
                valid += 1
        self.assertEqual(valid, 10)

    def test_talon_temperature_drift_rejected(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("talon_mass_right", self.changed("talon_mass_right", "temperature", 0.88), self.canon)

    def test_mink_constructor_default_cannot_replace_readme(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("min_k", self.changed("min_k", "tau", 2.0), self.canon)

    def test_legacy_top_k_rejected(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("talon_mass_right", self.changed("talon_mass_right", "external_top_k", 50), self.canon)

    def test_second_baseline_rejected(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("baseline_t085", {}, self.canon)

    def test_mirostat_feedback_removal_rejected(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("mirostat_original", self.changed("mirostat_original", "state_update", None), self.canon)

    def test_eta_not_replaced_by_another_papers_setting(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("eta_sampling", self.changed("eta_sampling", "eta_cutoff", 0.0009), self.canon)

    def test_ees_not_silently_admitted(self):
        with self.assertRaises(RecipeDrift):
            verify_effective_recipe("ees", {"theta": 1.0}, self.canon)

    def test_changed_canon_bytes_rejected(self):
        raw = Path(__file__).with_name(CANON_FILE).read_bytes()
        with self.assertRaises(RecipeDrift):
            verify_bytes(raw + b" ")

    def test_seeds_and_single_baseline(self):
        self.assertEqual(self.canon["seeds"], [64, 12, 24, 48, 96])
        self.assertEqual(self.canon["baseline_policy"]["count"], 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--profile")
    parser.add_argument("--effective-json", type=Path)
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GuardTests))
        raise SystemExit(0 if result.wasSuccessful() else 1)
    canon = load_canon()
    if args.profile:
        if args.effective_json is None:
            parser.error("--effective-json is required: do not substitute the expected recipe for observed runtime values")
        print(json.dumps(verify_effective_recipe(args.profile, json.loads(args.effective_json.read_text(encoding="utf-8")), canon), indent=2))
    else:
        print(json.dumps({"canon_id": CANON_ID, "sha256": CANON_SHA256, "state": "BYTES_VERIFIED_NOT_EXECUTED"}, indent=2))


if __name__ == "__main__":
    main()
