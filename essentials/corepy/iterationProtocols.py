# iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
# iterator = iter(iterable)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)

def first(iterable):
    iterable = iter(iterable)
    try:
            return next(iterable)
    except StopIteration:
      raise ValueError("iteable is empty")
  

print(first(["1st", "2nd", "3rd"]))  # List

print(first({"1st", "2nd", "3rd"}))  # Set

print(first(set()))   # Empty set

