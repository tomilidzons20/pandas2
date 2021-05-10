import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# Zad1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

imiona = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(imiona, header=0)
print("\nZad1")

grupa = df.groupby(["Rok"]).agg({"Liczba": ["sum"]})
wykres = grupa.plot()
wykres.set_ylabel("Liczba urodzen w danym roku")
plt.show()

# Zad2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

print("\nZad2")
grupa1 = df.groupby(["Plec"]).agg({"Liczba": ["sum"]})
wykres1 = grupa1.plot.bar()
wykres1.set_ylabel("100 tys")
plt.xticks(rotation=0)
plt.show()

# Zad3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

print("\nZad3")
grupa2 = df.groupby("Rok").agg({"Liczba": ["sum"]})
grupa2 = grupa2.sort_values(by=["Rok"], ascending=False).head(5)
wykres2 = grupa2.plot.pie(subplots=True, autopct="%.2f %%", fontsize=20, figsize=(6, 6), legend=(0, 0))
plt.legend(loc="lower left")
plt.title("Liczba urodzonych ch i dz w ostatnich 5 latach", loc="center")
plt.show()

# Zad4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez
# poszczególnych sprzedawców (zbiór danych zamówienia.csv).

print("\nZad4")
pd = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
grupa3 = pd.groupby("Sprzedawca")["idZamowienia"].nunique()
wykres3 = grupa3.plot.bar()
wykres3.set_ylabel("Ilosc zamowien")
wykres3.set_xlabel("Sprzedawca")
plt.xticks(rotation=0)
plt.show()
