user_choice = -1


while user_choice != 0:
    
    print("\nMenyval:")
    print("Tryck 1 för att skapa en kund")
    print("Tryck 2 för att ett nytt konto")
    print("Tryck 0 för att avsluta")
    
    try:
        user_choice = int(input('Vad vill du göra? '))
    
    except ValueError:
        print("Ogiltigt val, försök igen med ett nummer")
        continue
    
    if user_choice == 1:
        print("Du har valt att skapa en kund")
    
    elif user_choice == 2:
        print("Du har valt att skapa ett nytt konto")
    
    elif user_choice == 0:
        print("Du har valt att avsluta programmet")
    
    else:
        print("Ogiltigt val, försök igen")
    