def tietoja(nimi, ikä, harrastus):
    tervehdys = f"Terve {nimi}, ikäsi on {ikä} ja suosikkiharrastus on {harrastus}."
    return tervehdys


henkilö = tietoja("Ulla", 43, "enduro")
print(henkilö)

"""
Parametrien välittäminen avainsanojen avulla.
Ohjelmoija voi antaa parametrien arvot (nimi = arvo)-pareina.
Parametreille voi antaa funktion määrityksessä myös oletusarvot.
"""

henkilö2 = tietoja(nimi="Pekka", ikä=23, harrastus="tennis")
print(henkilö2)

# Mitä, jos en tiedä jotain argumenttia? Miten voin kutsua funktiota?


def tietoja2(nimi, ikä, harrastus="ohjelmointi"):
    tervehdys = f"Terve {nimi}, ikäsi on {ikä} ja suosikkiharrastus on {harrastus}."
    return tervehdys


henkilö3 = tietoja2("Pekka", 23)
print(henkilö3)
