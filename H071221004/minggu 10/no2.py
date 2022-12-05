class Bunga:
    def __init__(self, jenis, beracun):
        self._jenis= jenis
        self._beracun= beracun

    def getjenis(self):
        return self._jenis

    def setjenis(self, jenis):
        self._jenis= jenis

    def mengeluarkan_bau(self):
        pass

class Rafflesia(Bunga):
    def __init__(self, jenis, beracun):
        super().__init__(jenis, beracun)

    def mengeluarkan_bau(self):
        print('bunga rafflesia mengeluarkan bau tidak sedap')

class Melati(Bunga):
    def __init__(self, jenis, beracun):
        super().__init__(jenis, beracun)

    def mengeluarkan_bau(self):
        print('bunga melati mengeluarkan bau harum')

a = Rafflesia("rafflesia", True)
b = Melati("melati", False)

a.mengeluarkan_bau()
b.mengeluarkan_bau()
