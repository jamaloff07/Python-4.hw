class Film:
    def __init__(self, ad, il, reyting):
        self.ad = ad
        self.il = il
        self.reyting = reyting

    @property
    def reyting(self):
        return self._reyting

    @reyting.setter
    def reyting(self, value):
        if not 0 <= value <= 10:
            raise ValueError("Reyting 0–10 aralığında olmalıdır")
        self._reyting = value

    def __str__(self):
        return f"{self.ad} ({self.il}) {self.reyting}"

    def __eq__(self, other):
        if not isinstance(other, Film):
            return NotImplemented
        return (self.ad, self.il) == (other.ad, other.il)

    def __hash__(self):
        return hash((self.ad, self.il))

    @classmethod
    def from_string(cls, text):
        ad, il, reyting = text.split("|")
        return cls(ad.strip(), int(il), float(reyting))


class FilmSiyahisi:
    def __init__(self):
        self.filmler = []

    def elave_et(self, film):
        self.filmler.append(film)

    def __len__(self):
        return len(self.filmler)

    def en_yaxsi(self):
        if not self.filmler:
            return None
        return max(self.filmler, key=lambda f: f.reyting)


if __name__ == "__main__":
    f = Film("Inception", 2010, 8.8)
    print(f)
    try:
        f.reyting = 12
    except ValueError as e:
        print("ValueError:", e)

    s = FilmSiyahisi()
    s.elave_et(Film.from_string("Inception|2010|8.8"))
    s.elave_et(Film.from_string("Interstellar|2014|8.6"))
    print(len(s))  # 2
    print(s.en_yaxsi())
    print(len({Film("A", 2000, 5), Film("A", 2000, 9)}))

