def adatszerzes(nev):
    with open(nev, "r", encoding="utf-8") as file:
        sorok = file.read().splitlines()
    return sorok


def rendez(sor):
    cipok = []
    if not sor:
        return cipok

    fejlec = sor[0].split(",")
    for i in sor[1:]:
        ertekek = i.split(",")
        cipo = {key: value.strip() for key, value in zip(fejlec, ertekek)}

        if "fullPrice" in cipo:
            cipo["fullPrice"] = float(cipo["fullPrice"])
        if "currentPrice" in cipo:
            cipo["currentPrice"] = float(cipo["currentPrice"])

        cipok.append(cipo)
    return cipok


def main():
    fajlnev = "sneakers.csv"

    cipok = rendez(adatszerzes(fajlnev))
    rendszerezesi_lehetosegek = {
        "1": "title",
        "2": "color_breif",
        "3": "fullPrice",
        "4": "currentPrice",
        "5": "publish_date"
    }

    print("Válassz, melyik szempont alapján rendezzem a cipőket:")
    for kulcs, ertek in rendszerezesi_lehetosegek.items():
        print(f"{kulcs} - {ertek}")

    valasztas = input("Add meg a lehetőség számát: ")

    if valasztas in rendszerezesi_lehetosegek:
        ertek = rendszerezesi_lehetosegek[valasztas]
        rendszerezett_cipok = sorted(cipok, key=lambda x: x[ertek])
        for cipo in rendszerezett_cipok:
            print(cipo)

    else:
        print("Érvénytelen választás!")


main()
