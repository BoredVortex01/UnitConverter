def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

choice = input("Convert (1) km to miles or (2) Celsius to Fahrenheit: ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    print(f"{km} km is equal to {km_to_miles(km):.2f} miles.")
elif choice == "2":
    celsius = float(input("Enter Celsius: "))
    print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F.")
else:
    print("Invalid choice.")
