def hanoi(n, from_rod, to_rod, aux):
    if(n==1):
        print( "move ", n," from  ", from_rod, "to", to_rod)
        return

    hanoi(n-1, from_rod, aux, to_rod)
    print("move ", n, " from  ", from_rod, "to", to_rod)
    hanoi(n-1, aux, to_rod, from_rod)

hanoi(3, "A", "C", "B")