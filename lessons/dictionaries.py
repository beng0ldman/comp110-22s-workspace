"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary (using dict as a constructor function)
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a literal representation
print(schools)

# Access a value by its key -- "lookup"
# {schools['UNC']} is a subscription notation
print(f"UNC has {schools['UNC']} students")

# To remove a key-value pair from a dictionary by its key, use pop
schools.pop("Duke")

# Test for the existence of a key (after popping Duke)
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literals
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# print(schools["UNCC"])
# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
