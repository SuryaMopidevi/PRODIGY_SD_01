def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    print("Welcome to the Temperature Converter!")
    print("Choose the input temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} °F = {celsius:.2f} °C = {kelvin:.2f} K")

    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} K = {celsius:.2f} °C = {fahrenheit:.2f} °F")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    convert_temperature()
