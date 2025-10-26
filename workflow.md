#1) Neuen Tagesordner anlegen

mkdir -p python/2025-10-26-basic-syntax

#oder für Django:

#mkdir -p django/2025-10-27-first-project

#2) Dateien hinzufügen (Übungen/Notizen)

echo "Notizen zu Listen, Dicts, Loops" > python/2025-10-26-basic-syntax/notes.md
printf 'print("hello")\n' > python/2025-10-26-basic-syntax/exercises.py

#3) Commit & Push

git add .
git commit -m "Python: Basic Syntax – Lists/Dicts/Loops (Notizen + Übungen)"
git push
