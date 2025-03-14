# RSPEC-1128 Unused imports should be removed
from mymodule import foo, qix  # Noncompliant: bar is unused

foo()
qix()