def generate_profile(age: int) -> str:
    """Return a life stage string for the given age.

    Args:
        age (int): User's age.

    Returns:
        str: Life stage ("Child", "Teenager", "Adult", or "Invalid age").
    """
    if 0 <= age <= 12:
        return "Child"
    if 13 <= age <= 19:
        return "Teenager"
    if age >= 20:
        return "Adult"
    return "Invalid age"


def collect_hobbies() -> list[str]:
    """Collect hobbies from user input until 'stop' is typed.

    Returns:
        List[str]: List of  hobbies.
    """

    hobbies: list[str] = []
    while True:
        word = input("Enter a favorite hobby or type 'stop' to finish: ")
        if word.lower() == "stop":
            break
        hobbies.append(word)
    return hobbies


def print_profile(profile: dict[str, str | int | list[str]]) -> None:
    """Prints user profile.

    Args:
        profile (dict): Dictionary contains info about user
    """
    print("---")
    print("Profile Summary:")
    print(f"Name: {profile['Name']}")
    print(f"Age: {profile['Age']}")
    print(f"Life Stage: {profile['Stage']}")

    hobbies = profile["Hobbies"]
    # hobbies should be list[str]
    assert isinstance(hobbies, list)

    if not hobbies:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for h in hobbies:
            print(f"- {h}")
    print("---")


def main() -> None:
    """Collect user data, build profile dictionary, print it."""
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year

    hobbies: list[str] = collect_hobbies()

    life_stage = generate_profile(current_age)

    user_profile: dict[str, str | int | list[str]] = {
        "Name": user_name,
        "Age": current_age,
        "Stage": life_stage,
        "Hobbies": hobbies,
    }

    print_profile(user_profile)


if __name__ == "__main__":
    main()
