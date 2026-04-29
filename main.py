import datetime

def check_covid():
    print("\n=== COVID Symptom Checker ===")

    name = input("Enter your name: ")

    # Temperature input
    try:
        temp = float(input("Enter your body temperature (°C): "))
    except ValueError:
        print("Invalid input! Setting default temperature 36.5°C")
        temp = 36.5

    # Symptoms
    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    breathing = input("Breathing difficulty? (yes/no): ").lower()
    fatigue = input("Fatigue? (yes/no): ").lower()
    smell = input("Loss of smell/taste? (yes/no): ").lower()

    # Score system
    score = 0

    if temp > 37.5:
        score += 2
    if fever == "yes":
        score += 2
    if cough == "yes":
        score += 2
    if breathing == "yes":
        score += 3
    if fatigue == "yes":
        score += 1
    if smell == "yes":
        score += 2

    # Result logic
    if score >= 6:
        result = "High Risk"
    elif score >= 3:
        result = "Moderate Risk"
    else:
        result = "Low Risk"

    print(f"\n{name}, Your Result: {result}")

    # Save results to file
    with open("results.txt", "a") as file:
        file.write(
            f"{datetime.datetime.now()} | {name} | Temp:{temp} | Score:{score} | {result}\n"
        )


# Loop for multiple users
def main():
    while True:
        check_covid()

        again = input("\nCheck another person? (yes/no): ").lower()
        if again != "yes":
            print("Exiting program. Stay safe!")
            break


if __name__ == "__main__":
    main()
