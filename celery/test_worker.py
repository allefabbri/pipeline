#! /usr/bin/env python3

from tasks_with_results import add
#from tasks import add

kw = {
  'x':4,
  'y':9,
  'sleep':4,
}
result = add.delay(**kw)
tot = result.get(timeout=5)
print(tot)
