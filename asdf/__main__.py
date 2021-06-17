print("in asdf.__main__, __name__ is", __name__, "and __package__ is", __package__)

import sys
print("   and sys.args contains", repr(sys.argv))
print("   and asdf is in sys.modules?", 'asdf' in sys.modules)
