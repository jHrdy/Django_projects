import random
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noteproject.settings")
django.setup()

from noteapp.models import Author, Notes

# Sample data for generating test entries
titles = [
    "Calculus I",
    "Classical Mechanics",
    "Introduction to Programming"
]

descriptions = [
    "Notes on differential and integral calculus covering limits, derivatives, and integrals.",
    "Notes on Newtonian mechanics, including laws of motion, energy, and momentum.",
    "Notes on basic programming concepts using Python, including variables, control structures, and functions."
]

first_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
last_names = ["Johnson", "Smith", "Brown", "Williams", "Jones"]
subjects = ["maths", "physics", "programming", "other"]

def generate_authors(count):
    for _ in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        Author.objects.create(first_name=first_name, last_name=last_name)

def generate_notes(count):
    for _ in range(count):
        title = random.choice(titles)
        about = random.choice(descriptions)  # Náhodný výber popisu z `descriptions`
        subject = random.choice(subjects)
        author = Author.objects.order_by('?').first()  # Náhodný výber autora
        Notes.objects.create(title=title, about=about, author=author, subject=subject)

generate_authors(10)
generate_notes(10)

print("Test data generated successfully.")
