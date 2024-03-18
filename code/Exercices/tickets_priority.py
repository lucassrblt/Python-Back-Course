
ticket_priority = {
    1 : "Critique",
    2 : "Forte",
    3 : "Moyenne",
    4 : "Faible"
}

def ticket_prority(ticket):
    code, ticket_name = ticket.split("-") # Récupère le code et le nom du ticket
    if code and ticket_name:
        priority = ticket_priority.get(int(code)) # Transforme le code en int et récupère la valeur correspondante
        if priority:
            print(f"Le ticket {ticket_name} est de priorité {priority}")
        else:
            print("Code de priorité non reconnu")
    else:
        print("Ticket non reconnu")

user_ticket = input("Entrez votre ticket : ")
ticket_priority(user_ticket)