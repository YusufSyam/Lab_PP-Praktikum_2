class Buku:
    def __init__(self, judul, penulis):
        self._judul = judul
        self._penulis = penulis

    def getJudul(self):
        return self._judul

    def setJudul(self, judul):
        self._judul= judul
        

    def getPenulis(self):
        return self._penulis

    def setpenulisl(self, penulis):
        self._penulisl= penulis

    def membandingkan(self):
        pass

class Dilan(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def membandingkan(self, target):
        print("Isi Novel Dilan tak semenarik " + target.getJudul()+ "!")

class Skripsi(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def membandingkan(self, target):
        print("Skripsi sangat mempusingkan dibanding " + target.getJudul())

a= Dilan("Dilan", 'abc')
b = Skripsi("Skripsi", 'Yusuf')

b.membandingkan(a)
a.membandingkan(b)