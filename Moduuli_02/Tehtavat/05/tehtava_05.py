leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

leiviskat_luodit = leiviskat * 640
naulat_luodit = naulat * 32

luodit_sum = luodit + leiviskat_luodit + naulat_luodit

luodit_sum_grams_total = luodit_sum * 13.3

luodit_sum_kilograms_whole = int(luodit_sum_grams_total) // 1000
luodit_sum_kilograms_remainder = luodit_sum_grams_total % 1000

print(f"\nMassa nykymittojen mukaan (grammat pyöristetty toisen desimaalin tarkkuuteen)\n"
      f"{luodit_sum_kilograms_whole} kilogrammaa ja {luodit_sum_kilograms_remainder:.2f} grammaa.")
