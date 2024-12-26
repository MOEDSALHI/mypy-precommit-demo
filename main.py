from typing import Sequence, Union


def calculate_average(numbers: Sequence[Union[int, float]]) -> float:
    """Calcule la moyenne d'une liste de nombres."""
    if not numbers:
        raise ValueError("La liste ne peut pas être vide.")
    return sum(numbers) / len(numbers)


def main() -> None:
    """Point d'entrée du programme."""
    nums = [10, 20, 30, 40, 50]  # Une erreur ici : "50" est une chaîne, pas un float.
    print(f"La moyenne est : {calculate_average(nums)}")


if __name__ == "__main__":
    main()
