from .leakage import INTENTION as LEAK_INTENTION, HARNESS as LEAK_HARNESS

ATTACKS = {
    "": {"intention": "", "harness": ""},
    "leakage": {"intention": LEAK_INTENTION, "harness": LEAK_HARNESS}
}