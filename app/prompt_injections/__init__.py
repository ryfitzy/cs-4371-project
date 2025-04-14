from .leakage import INTENTION as LEAK_INTENTION, HARNESS as LEAK_HARNESS
from .manipulation import INTENTION as MANIP_INTENTION, HARNESS as MANIP_HARNESS

ATTACKS = {
    "": {"intention": "", "harness": ""},
    "leakage": {"intention": LEAK_INTENTION, "harness": LEAK_HARNESS},
    "manipulation": {"intention": MANIP_INTENTION, "harness": MANIP_HARNESS}
}