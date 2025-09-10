def input_details(day: int):
    n: int = int(input(f"Enter the number of people attended on day {day}: "))
    day: set = set()
    for i in range(n):
        day.add(input(f"Enter the email address of the candidate {i+1}: ").lower())
    return day

# Total number of unique attendees
def unique_attendees(day1: set, day2: set, day3: set) -> int:
    return len(day1 | day2 | day3)

# Attendees attended on all three days
def common_attendees(day1: set, day2: set, day3: set) -> int:
    return day1 & day2 & day3

# Unique attendees
def one_day_attended(day1: set, day2: set, day3: set):
    return (day1 - (day2 | day3)) | (day2 - (day1 | day3)) | (day3 - (day1 | day2))

# Pairwise overlaps
def pairwise_overlaps(day1: set, day2: set, day3: set):
    print(f"{len(day1 & day2)} members have attended on day 1 and 2")
    print(f"{len(day3 & day2)} members have attended on day 2 and 3")
    print(f"{len(day1 & day3)} members have attended on day 1 and 3")

# Report
def report(day1: set, day2: set, day3: set):
    print("Attendees on day1:", sorted(day1))
    print("Attendees on day2:", sorted(day2))
    print("Attendees on day3:", sorted(day3))
    
    print(f"{len(day1)} members attended on day1")
    print(f"{len(day2)} members attended on day2")
    print(f"{len(day3)} memebers attended on day3")

day1 = input_details(1)
day2 = input_details(2)
day3 = input_details(3)

print(f"There are {unique_attendees(day1, day2, day3)} attendees on 3 days")

print("Attendees who attended all the three days are: ")
for attendee in common_attendees(day1, day2, day3):
    print(attendee, end=" ")
else:
    print()
    
print("Attendees who attended exactly one day are: ")
for attendee in one_day_attended(day1, day2, day3):
    print(attendee, end=" ")
else: print()

pairwise_overlaps(day1, day2, day3)

report(day1, day2, day3)