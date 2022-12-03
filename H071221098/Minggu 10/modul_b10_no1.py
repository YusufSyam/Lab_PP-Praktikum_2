import re
# from prettytable import PrettyTable
_Data = []
while True:
    print(100*"="+"""\nPILIHAN LAYANAN
1. Detail Anda
2. Ubah Nama
3. Jumlah Data Pada File
4. Save Data pada File
5. Buat Data Baru
6. Keluar """)
    _inputan = int(input(100*"="+"\nPilihan : ")); 
    if _inputan == 1: # Menampilkan Data Diri yang ada dalam list _Data
        if len(_Data) > 0: 
            print(100*"=")
            for i in range(len(_Data)):
                for y in range(len(_Data[0])):
                    print(f'{_Data[i][y]}')
        else:
            print(100*"="+"\nData saat ini kosong!\n"+100*"=")
    elif _inputan == 2: # Mengubah nama dalam list _Data
        if len(_Data) != 0:
            print(100*"=")
            for i in range(len(_Data)):
                for y in range(len(_Data[0])):
                    if y == 1 or y == 2: 
                        continue
                    print(f'Urutan {i+1} {_Data[i][y]}')
            _newName = list(map(str, input("Masukkan Index dan nama baru (Urutan NamaBaru) : ").split()))
            _Data[int(_newName[0])-1][0] = "Nama : "+_newName[1]
        elif len(_Data) == 0:
            print(100*"="+"\nData Tidak Ditemukan!\n"+100*"=")
    elif _inputan == 3: # Menampilkan jumlah data pada file <namaFile>.txt
        _file = input("Masukkan fIle : ")+".txt"
        try:
            with open(_file) as baca:
                dataFILE = re.findall(r"@student.unhas.ac.id", baca.read())
            print(f"Jumlah Data adalah {dataFILE.count('@student.unhas.ac.id')}")
        except FileNotFoundError:
            print(100*"="+f"\nTidak Terdapat File Dengan Nama {_file}")
            print("Jumlah data pada file = 0\n"+100*"=")
    elif _inputan == 4: # Menulis data pada list ke File <namaFile>.txt
        if len(_Data) == 0: 
            print(100*"="+"\nData Sata Ini Kosong!\n"+100*"=")
        else:
            _FILE = input("Nama File : ")+".txt"
            with open(_FILE, "a") as tulis:
                tulis.write("\n")
                for i in range(len(_Data)):
                    for y in range(len(_Data[0])):
                        tulis.write(_Data[i][y]+"\n")
                    tulis.write(100*"=")
                _Data = []
    elif _inputan == 5: # Memasukkan data baru kedalam list _Data
        nama = input(100*"="+"\nNama : "); print(100*"=")
        while True:
            Email = input("Email : ")
            if re.search(r"^[a-z0-9]{1,}@student[.]unhas[.]ac[.]id$", Email):
                break
            else:
                print(100*"="+"\nEmail Yang Anda Masukkan salah\n"+100*"=")
        while True:
            _Pass = input(100*"="+"\nMasukkan Password : "); print(100*"=")
            if len(_Pass) >= 8 and len(_Pass) <= 20:
                if re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', _Pass):
                    break
                else:
                    print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            else: 
                print("Password Harus Memiliki 8-20 Karakter")
        _Data.insert(len(_Data), ["Nama : " + nama,"E-mail : "+ Email, "Password : "+ _Pass]); print("Berhasil")
    elif _inputan == 6: # Keluar dari program/menyelesaikan while
        print(100*"="+"\nSampai Jumpa Lagi\n"+100*"=")
        break