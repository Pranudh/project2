class Movie:
    def __init__(self, title, available_tickets):
        self.title = title
        self.available_tickets = available_tickets

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = []
        self.users = []
        self.logged_in_user = None
        self.customers = {}  # Mapping from phone number to customer names
        self.init_users()

    def init_users(self):
        # Adding some default theater users
        self.users.append(User("theatre1", "theatre1@123", "theatre"))
        self.users.append(User("theatre2", "theatre2@123", "theatre"))

    def login(self):
        print("1. Customer Login")
        print("2. Theatre Login")
        choice = input("Enter choice: ")

        if choice == '1':
            phone_number = input("Enter phone number: ")
            if phone_number in self.customers:
                self.logged_in_user = User(phone_number, "", "customer")
                print(f"Login successful! Logged in as customer.")
                return True
            else:
                name = input("Enter your name to register: ")
                self.customers[phone_number] = name
                self.logged_in_user = User(phone_number, "", "customer")
                print(f"Registration successful! Logged in as customer.")
                return True
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            for user in self.users:
                if user.username == username and user.password == password:
                    self.logged_in_user = user
                    print(f"Login successful! Logged in as {self.logged_in_user.role}.")
                    return True
            print("Invalid username or password.")
            return False
        else:
            print("Invalid choice.")
            return False

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. View Movies")
            print("2. Book Ticket")
            print("3. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                self.view_movies()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def theatre_menu(self):
        while True:
            print("\nTheatre Menu:")
            print("1. Add Movie")
            print("2. Delete Movie")
            print("3. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_movie()
            elif choice == '2':
                self.delete_movie()
            elif choice == '3':
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def view_movies(self):
        if not self.movies:
            print("No movies available.")
            return
        print("\nAvailable Movies:")
        for idx, movie in enumerate(self.movies):
            print(f"{idx + 1}. {movie.title} - Tickets Available: {movie.available_tickets}")

    def book_ticket(self):
        self.view_movies()
        if not self.movies:
            return
        try:
            choice = int(input("Enter the movie number to book a ticket: "))
            if 1 <= choice <= len(self.movies):
                selected_movie = self.movies[choice - 1]
                if selected_movie.available_tickets > 0:
                    selected_movie.available_tickets -= 1
                    print(f"Ticket booked successfully for {selected_movie.title}.")
                else:
                    print("No tickets available for this movie.")
            else:
                print("Invalid movie number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def add_movie(self):
        title = input("Enter movie title: ")
        try:
            available_tickets = int(input("Enter number of available tickets: "))
            self.movies.append(Movie(title, available_tickets))
            print(f"Movie {title} added successfully with {available_tickets} tickets.")
        except ValueError:
            print("Invalid input. Tickets should be a number.")

    def delete_movie(self):
        self.view_movies()
        if not self.movies:
            return
        try:
            choice = int(input("Enter the movie number to delete: "))
            if 1 <= choice <= len(self.movies):
                selected_movie = self.movies.pop(choice - 1)
                print(f"Movie {selected_movie.title} deleted successfully.")
            else:
                print("Invalid movie number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            if not self.logged_in_user:
                print("\nWelcome to the Movie Ticket Booking System")
                print("1. Login")
                print("2. Exit")
                choice = input("Enter choice: ")

                if choice == '1':
                    if self.login():
                        if self.logged_in_user.role == "customer":
                            self.customer_menu()
                        elif self.logged_in_user.role == "theatre":
                            self.theatre_menu()
                elif choice == '2':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = MovieTicketBookingSystem()
    system.run()
