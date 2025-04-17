from .info_gathering import HARNESS as INFO_HARNESS
from .info_gathering import INTENTION as INFO_INTENTION
from .leakage import HARNESS as LEAK_HARNESS
from .leakage import INTENTION as LEAK_INTENTION
from .manipulation import HARNESS as MANIP_HARNESS
from .manipulation import INTENTION as MANIP_INTENTION
from .spam import HARNESS as SPAM_HARNESS
from .spam import INTENTION as SPAM_INTENTION
from .ethical_violation import HARNESS as ETHICAL_HARNESS
from .ethical_violation import INTENTION as ETHICAL_INTENTION

ATTACKS = {
    "": {"intention": "", "harness": ""},
    "leakage": {"intention": LEAK_INTENTION, "harness": LEAK_HARNESS},
    "manipulation": {"intention": MANIP_INTENTION, "harness": MANIP_HARNESS},
    "info_gathering": {"intention": INFO_INTENTION, "harness": INFO_HARNESS},
    "spam": {"intention": SPAM_INTENTION, "harness": SPAM_HARNESS},
    "ethical_violation": {"intention": ETHICAL_INTENTION, "harness": ETHICAL_HARNESS},
}
