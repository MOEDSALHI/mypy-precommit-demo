# Projet : mypy-precommit-demo

Ce projet illustre comment configurer et utiliser **mypy** et **pre-commit** pour améliorer la qualité du code Python, ainsi que l’intégration avec **GitHub Actions** pour l’automatisation.

## Objectif

- Détecter les erreurs de typage dans Python avec **mypy**.
- Automatiser les vérifications avec **pre-commit**.
- Exécuter les tests automatiquement lors de chaque push ou pull request avec **GitHub Actions**.

---

## Prérequis

1. **Git** : Assurez-vous que Git est installé.
2. **Python 3.11+** : Une version récente de Python doit être installée.
3. **Un dépôt GitHub** : Pour utiliser GitHub Actions.

---

## Étapes de configuration

### 1. Initialisation du projet

1. **Créez un répertoire pour le projet** :

   ```bash
   mkdir mypy-precommit-demo
   cd mypy-precommit-demo
   ```

2. **Initialisez un dépôt Git** :

   ```bash
   git init
   ```

3. **Créez un environnement virtuel Python** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

4. **Installez les dépendances** :

   ```bash
   pip install mypy pre-commit
   ```

### 2. Configuration de pre-commit

1. Créez le fichier `.pre-commit-config.yaml` à la racine du projet :

   ```yaml
   repos:
     - repo: https://github.com/pre-commit/mirrors-mypy
       rev: v1.14.0
       hooks:
         - id: mypy
   ```

   **Options supplémentaires possibles** :
   - Vous pouvez configurer plusieurs hooks dans ce fichier pour inclure des outils comme `flake8` ou `black`.
   - Exemple :

     ```yaml
     repos:
       - repo: https://github.com/pre-commit/mirrors-mypy
         rev: v1.14.0
         hooks:
           - id: mypy
       - repo: https://github.com/psf/black
         rev: 23.1.0
         hooks:
           - id: black
       - repo: https://gitlab.com/pycqa/flake8
         rev: 5.0.4
         hooks:
           - id: flake8
     ```

2. Installez les hooks pre-commit :

   ```bash
   pre-commit install
   ```

   **Commandes importantes** :

   - `pre-commit install` : Active les hooks pour chaque commit.
   - `pre-commit run --all-files` : Exécute manuellement les hooks sur tous les fichiers.

### 3. Configuration de mypy

1. Créez un fichier `mypy.ini` pour personnaliser les règles de typage :

   ```ini
   [mypy]
   python_version = 3.11
   check_untyped_defs = True
   disallow_untyped_calls = True
   ignore_missing_imports = True
   ```

   **Options supplémentaires possibles** :
   - `warn_unused_configs = True` : Avertit en cas de configuration inutile.
   - `plugins =` : Permet d’ajouter des plugins pour des frameworks spécifiques comme Django ou SQLAlchemy.
   - Exemple pour Django :

     ```ini
     plugins = mypy_django_plugin.main
     ```

   - `strict = True` : Active toutes les options strictes pour renforcer les vérifications.

### 4. Ajout d’un exemple de code

Créez un fichier `main.py` :

```python
from typing import Sequence, Union

def calculate_average(numbers: Sequence[Union[int, float]]) -> float:
    """Calcule la moyenne d'une liste de nombres."""
    if not numbers:
        raise ValueError("La liste ne peut pas être vide.")
    return sum(numbers) / len(numbers)

def main() -> None:
    """Point d'entrée du programme."""
    nums = [10, 20, 30, 40, 50]
    print(f"La moyenne est : {calculate_average(nums)}")

if __name__ == "__main__":
    main()
```

### 5. Configuration de GitHub Actions

1. Créez le répertoire `.github/workflows/` :

   ```bash
   mkdir -p .github/workflows
   ```

2. Créez un fichier `ci.yml` :

   ```yaml
   name: Python CI

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     lint-and-type-check:
       name: Run pre-commit and mypy
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: 3.11

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install pre-commit mypy

         - name: Run pre-commit
           run: pre-commit run --all-files

         - name: Run mypy
           run: mypy main.py
   ```

   **Options supplémentaires possibles** :
   - Ajouter des étapes pour d'autres outils comme `pytest` :

     ```yaml
     - name: Run tests
       run: pytest
     ```

3. Ajoutez le fichier de workflow au dépôt :

   ```bash
   git add .github/workflows/ci.yml
   git commit -m "Ajout du workflow GitHub Actions pour mypy et pre-commit"
   ```

### 6. Synchronisation avec GitHub

1. Ajoutez votre dépôt distant :

   ```bash
   git remote add origin <URL_DU_DEPOT_GITHUB>
   ```

2. Poussez la branche principale (`main`) :

   ```bash
   git push --set-upstream origin main
   ```

---

## Fonctionnement des outils

### mypy

**mypy** est un vérificateur de typage statique pour Python. Il vérifie que le code respecte les annotations de type avant l'exécution.

- Documentation : [https://mypy.readthedocs.io](https://mypy.readthedocs.io)

### pre-commit

**pre-commit** permet d’exécuter des scripts automatiquement avant chaque commit pour valider le code.

- Documentation : [https://pre-commit.com](https://pre-commit.com)

### GitHub Actions

**GitHub Actions** permet d’automatiser les workflows, comme l’exécution de tests ou de vérifications.

- Documentation : [https://github.com/features/actions](https://github.com/features/actions)

---

## Validation finale

1. Effectuez un commit avec des erreurs pour voir **pre-commit** et **mypy** en action.
2. Poussez vers GitHub pour vérifier que GitHub Actions exécute les tests automatiquement.

---

## Structure du projet

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── .pre-commit-config.yaml
├── main.py
├── mypy.ini
├── README.md
└── venv/
```

---

Avec cette configuration, vous avez mis en place une intégration continue robuste pour un projet Python. 🎉

