import pprint


def beolvas_csv(fajlnev):
    with open(fajlnev, encoding='utf-8') as fajl:
        sorok = fajl.read().splitlines()
    fejlec = sorok[0].split(",")  # Első sor: oszlopnevek
    adatok = [sor.split(",") for sor in sorok[0:]]  # Adatok feldolgozása listába
    return fejlec, adatok


def kiir_rendezesi_lehetosegek():
    """ Kiírja a választható rendezési szempontokat """
    lehetosegek = {
        "1": "title",
        "2": "color_breif",
        "3": "fullPrice",
        "4": "currentPrice",
        "5": "publish_date"
    }
    print("\nVálassz, melyik szempont alapján rendezzem a cipőket?")
    for kulcs, ertek in lehetosegek.items():
        print(f"{kulcs} - {ertek}")
    return lehetosegek


def kivalaszt_rendezesi_szempont(lehetosegek):
    valasztas = input("Add meg a lehetőség számát! ").strip()
    if valasztas not in lehetosegek:
        print("Érvénytelen választás! Kérlek, egy számot adj meg a listából.")
        exit()
    return lehetosegek[valasztas]


def rendez_adatok(fejlec, adatok, oszlop_nev):

    if oszlop_nev not in fejlec:
        print(f"Hiba: Az oszlop '{oszlop_nev}' nem található az adatokban.")
        exit()

    return sorted(adatok, key=lambda cipo: cipo[fejlec.index(oszlop_nev)])


def main():
    csv_fajl = "sneakers.csv"
    fejlec, cipok = beolvas_csv(csv_fajl)
    lehetosegek = kiir_rendezesi_lehetosegek()
    oszlop_nev = kivalaszt_rendezesi_szempont(lehetosegek)
    rendezett_cipok = rendez_adatok(fejlec, cipok, oszlop_nev)

    for cipo in rendezett_cipok:
        cipo_vegso = {}
        for i in range(len(fejlec)):
            cipo_vegso[fejlec[i]] = cipo[i]
        pprint.pprint(cipo_vegso)


main()
