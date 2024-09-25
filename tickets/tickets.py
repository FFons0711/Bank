def give_ticket():
    for n in range(1, 20):
        yield n

ticket = give_ticket()

def decorator():
    return f"Ticket - {next(ticket)}"