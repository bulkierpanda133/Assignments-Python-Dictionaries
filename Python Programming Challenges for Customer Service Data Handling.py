#Task 1: Customer Service Ticket Tracker



# Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets, customer_name, issue_description):
    """Open a new service ticket."""
    ticket_id = f"Ticket{str(len(tickets) + 1).zfill(3)}"
    tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
    print(f"New ticket opened with ID: {ticket_id}")

def update_ticket_status(tickets, ticket_id, new_status):
    """Update the status of an existing ticket."""
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(tickets, status_filter=None):
    """Display all tickets or filter by status."""
    if not tickets:
        print("No tickets available.")
        return
    
    for ticket_id, details in tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            print(f"{ticket_id}: {details}")

def main():
    """Main function to run the ticket tracker program."""
    while True:
        print("\nCustomer Service Ticket Tracker")
        print("1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Filter tickets by status")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            issue_description = input("Enter issue description: ")
            open_ticket(service_tickets, customer_name, issue_description)
        elif choice == "2":
            ticket_id = input("Enter ticket ID to update: ")
            new_status = input("Enter new status (open/closed): ").lower()
            update_ticket_status(service_tickets, ticket_id, new_status)
        elif choice == "3":
            print("\nAll Tickets:")
            display_tickets(service_tickets)
        elif choice == "4":
            status_filter = input("Enter status to filter by (open/closed): ").lower()
            print(f"\nFiltered Tickets ({status_filter}):")
            display_tickets(service_tickets, status_filter)
        elif choice == "5":
            print("Exiting the Customer Service Ticket Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
