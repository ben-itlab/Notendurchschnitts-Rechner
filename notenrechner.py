# ==================================================
# Projekt: Notendurchschnitts-
# Beschreibung:
# Dieses Programm berechnet den Durchschnitt
# mehrerer Schulnoten.
#
# Der Benutzer gibt zunächst die Anzahl der
# Noten ein und anschließend die einzelnen Noten.
# Danach wird der Notendurchschnitt berechnet
# und eine passende Bewertung ausgegeben.
#
# Verwendete Konzepte:
# - Listen
# - Schleifen
# - Benutzereingaben
# - Bedingungen (if / elif / else)
# - Mathematische Berechnungen
# ==================================================

# Liste zum Speichern der eingegebenen Noten
noten = []

print("=== Notendurchschnitts-Rechner ===")

# Anzahl der Noten vom Benutzer abfragen
anzahl = int(input("Wie viele Noten möchtest du eingeben? "))

# Noten einlesen und in der Liste speichern
for i in range(anzahl):
    note = float(input(f"Note {i + 1}: "))
    noten.append(note)

# Durchschnitt berechnen
durchschnitt = sum(noten) / len(noten)

# Ergebnis ausgeben
print("\nErgebnis:")
print(f"Dein Notendurchschnitt beträgt: {durchschnitt:.2f}")

# Durchschnitt bewerten
if durchschnitt <= 1.5:
    print("Sehr gute Leistung!")
elif durchschnitt <= 2.5:
    print("Gute Leistung!")
elif durchschnitt <= 3.5:
    print("Befriedigende Leistung.")
else:
    print("Hier gibt es noch Verbesserungspotenzial.")
