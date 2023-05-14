"""
1▹ Stwórz krotkę zawierającą dane twojego pupila
(rodzaj zwierzecia, rasa, jak się wabi).
Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np.

“Mój pies, rasy border collie wabi się Dyzio”.
"""

zwierze = "ptasznik", "brachypelma", "Dyzio"

(rodzaj_zwierzecia, rasa, name) = zwierze

print(f'Mój {rodzaj_zwierzecia}, rasy {rasa} wabi się {name}.')