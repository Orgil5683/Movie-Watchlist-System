FAIL = "movies.txt"


def movies_unshih(fail):
    movies = []
    with open(fail, encoding="utf-8") as f:
        for mur in f:
            mur = mur.strip()
            if mur == "":
                continue
            heseg = mur.split(",")
            ner = heseg[0]
            angilal = heseg[1]
            unelgee = int(heseg[2])
            kino = {"ner": ner, "angilal": angilal, "unelgee": unelgee}
            movies.append(kino)
    return movies


def movies_haruulah(movies):
    dugaar = 1
    for kino in movies:
        print(dugaar, "-", kino["ner"], "(" + kino["angilal"] + ")", "-", kino["unelgee"], "/10")
        dugaar = dugaar + 1


def movie_haih(movies, ner):
    for kino in movies:
        if kino["ner"] == ner:
            return kino
    return None


def kino_nemeh(movies):
    ner = input("Kinonii ner: ").strip()
    olson = movie_haih(movies, ner)
    if olson != None:
        print("Kino ali hediin burtgegdsen bn.")
        return
    
    angilal = input("Torol: ").strip()
    unelgee = int(input("Unelgee (1-10): ").strip())
    shine_kino = {"ner": ner, "angilal": angilal, "unelgee": unelgee}

    movies.append(shine_kino)
    print("Nemegdsen:", ner)


def kino_ustgah(movies):
    ner = input("Kinonii ner ustgah: ").strip()
    olson = movie_haih(movies, ner)
    if olson == None:
        print("Kino oldoogui.")
        return 
    movies.remove(olson)
    print("Ustgagdlaa:", ner)


def dund_ur_haruulah(movies):
    if len(movies) == 0:
        print("List hooson baina.")
        return
    niit = 0
    for kino in movies:
        niit = niit + kino["unelgee"]
    dund = niit / len(movies)
    print("Dundaj unelgee:", dund)


def hadgalah(movies, fail):
    with open(fail, "w", encoding="utf-8") as f:
        for kino in movies:
            mur = kino["ner"] + "," + kino["angilal"] + "," + str(kino["unelgee"])
            f.write(mur + "\n")
    print("Hadgalagdsan:", fail)
    return fail


def ajilluulah():
    movies = movies_unshih(FAIL)

    if not movies:
        print("Movies fail baihgui baina, dahin shalgana uu.")
        return

    while True:
        print()
        print("===== MOVIE WATCHLIST =====")
        print("1 - Buh uzsen kino haruulah")
        print("2 - Kino nemeh")
        print("3 - Kino ustgah")
        print("4 - Uzsen kinonii unelgeenii dundaj haruulah")
        print("5 - Hadgalah")
        print("0 - Garah")
        songolt = input("Songolt: ").strip()

        if songolt == "1":
            movies_haruulah(movies)
        elif songolt == "2":
            kino_nemeh(movies)
        elif songolt == "3":
            kino_ustgah(movies)
        elif songolt == "4":
            dund_ur_haruulah(movies)
        elif songolt == "5":
            hadgalah(movies, FAIL)
        elif songolt == "0":
            print("Bye.")
            break
        else:
            print("Buruu hariult.")


if __name__ == "__main__":
    ajilluulah()
