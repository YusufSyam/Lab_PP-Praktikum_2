club_A = ["R. Madrid", "Bayern" , "M. City" , "PSG" , "Persija" , "Arsenal" , "Ajax" , "Chelsea", "Inter"]
club_B = ["Barca" , "Dortmund", "M. United", "PSM Makassar", "Bhayangkara", "Liverpool", "Tottenham", "Juventus", "Atletico"]
n = input()

for i in range (len(club_A)):
    if n == club_A[i]:
        print(club_B[i])
        print(i+1)
    elif n == club_B[i]:
        print(club_A[i])
        print(i+1)
