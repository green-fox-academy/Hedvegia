from fleet import Fleet
from thing import Thing

fleet = Fleet()
t1 = Thing("Get milk")
t2 = Thing("Remove the obstacles")
t3 = Thing("Stand up")
t4 = Thing("Eat lunch")
t3.completed = True
t4.completed = True

fleet.add(t1)
fleet.add(t2)
fleet.add(t3)
fleet.add(t4)
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)