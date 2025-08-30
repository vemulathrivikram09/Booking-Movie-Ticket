from Movie_Logic import display_movies,select_movie, calculate_total, print_ticket

# Ask user for input every time

display_movies()
movie = select_movie()

if movie:
    tickets = int(input("Enter number of tickets: "))
    total, discount_text, final = calculate_total(movie, tickets)
    print_ticket(movie, tickets, total, discount_text, final)