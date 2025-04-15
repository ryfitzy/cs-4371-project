from .leakage import INTENTION as LEAK_INTENTION, HARNESS as LEAK_HARNESS
from .manipulation import INTENTION as MANIP_INTENTION, HARNESS as MANIP_HARNESS
from .info_gathering import INTENTION as INFO_INTENTION, HARNESS as INFO_HARNESS
from .spam import INTENTION as SPAM_INTENTION, HARNESS as SPAM_HARNESS

ATTACKS = {
    "": {"intention": "", "harness": ""},
    "leakage": {"intention": LEAK_INTENTION, "harness": LEAK_HARNESS},
    "manipulation": {"intention": MANIP_INTENTION, "harness": MANIP_HARNESS},
    "info_gathering": {"intention": INFO_INTENTION, "harness": INFO_HARNESS},
    "spam": {"intention": SPAM_INTENTION, "harness": SPAM_HARNESS},
}