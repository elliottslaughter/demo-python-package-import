print("in asdf.__main__, __name__ is", repr(__name__), "and __package__ is", repr(__package__))

import sys
print("   and sys.args contains", repr(sys.argv))
print("   and asdf is in sys.modules?", 'asdf' in sys.modules)
