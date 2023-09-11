leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

leiviskat_luodit = leiviskat * 640
naulat_luodit = naulat * 32

luodit_sum = luodit + leiviskat_luodit + naulat_luodit

grams_total = luodit_sum * 13.3
kilograms_whole = int(grams_total) // 1000
kilograms_remainder = grams_total % 1000

print(f"\nMassa nykymittojen mukaan (grammat pyöristetty toisen desimaalin tarkkuuteen)\n"
      f"{kilograms_whole} kilogrammaa ja {kilograms_remainder:.2f} grammaa.")
