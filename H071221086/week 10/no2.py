from Zoo import Kucing, Anjing
kucing = Kucing("oren")
anjing = Anjing("coklat")

print("-"*30)
print("--- Cara kucing bergerak ---")
kucing.bergerak()
print("-"*30)
print("--- Cara anjing bergerak ---")
print("-"*30)
anjing.bergerak()

print("-"*30)
print("--- Cara kucing bertarung ---")
kucing.bertarung()
print("-"*30)

print("--- Cara anjing bertarung ---")
anjing.bertarung()
print("-"*30)

print("Kucing serang anjing")
print("--- Darah anjing sebelum diserang ---")
anjing.cekDarah()
kucing.serang(anjing)
print("--- Darah anjing setelah diserang ---")
anjing.cekDarah()


