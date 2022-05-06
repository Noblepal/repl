counties_in_kenya = [
    "Nairobi",
    "Nakuru",
    "Mombasa",
    "Kisumu"
]

# Final list
print(f"Initial list: {counties_in_kenya}")

print(f"First item: {counties_in_kenya[0]}")  # First item in the list
print(f"Last item: {counties_in_kenya[-1]}")  # Last item in the list

# Change an item
counties_in_kenya[2] = "Machakos"
print(f"Changed item: {counties_in_kenya[2]}")

# Add to the list
counties_in_kenya.append("Bungoma")
print(f"Added item: {counties_in_kenya[-1]}")

# Final list
print(f"Final list: {counties_in_kenya}")
