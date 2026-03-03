#Experion Coding Qn

'''
Got it 👍 You want **one clean interview question**, not breakdown, not rounds.

Here it is — strong, complete, and realistic:

---

## 🏸 OOP / LLD Interview Question

Design a **Badminton Court Booking System** for a sports complex with the following requirements:

* The complex has:

  * **2 Singles Courts**
  * **1 Doubles Court**
* A user must provide:

  * Name
  * Contact number
  * Number of players
  * Desired time slot
* Rules:

  * Singles court → maximum 2 players
  * Doubles court → exactly 4 players
* The system must:

  * Check if a court is available at the given time
  * Prevent double booking of the same court at the same time
  * Automatically generate a **unique ticket ID** for each booking
  * Store booking details
  * Display confirmation after successful booking

'''
import uuid
class Booking:
    def __init__(self, user_name, contact, players, court_type, time_slot):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.user_name = user_name
        self.contact = contact
        self.players = players
        self.court_type = court_type
        self.time_slot = time_slot

    def display_booking(self):
        print("\nBooking Confirmed!")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Name: {self.user_name}")
        print(f"Contact: {self.contact}")
        print(f"Players: {self.players}")
        print(f"Court Type: {self.court_type}")
        print(f"Time Slot: {self.time_slot}")


class Court:
    def __init__(self, court_id, court_type):
        self.court_id = court_id
        self.court_type = court_type
        self.bookings = {}  # time_slot → Booking

    def is_available(self, time_slot):
        return time_slot not in self.bookings

    def book(self, booking):
        self.bookings[booking.time_slot] = booking


class BadmintonCenter:
    def __init__(self):
        self.courts = [
            Court("S1", "Singles"),
            Court("S2", "Singles"),
            Court("D1", "Doubles")
        ]

    def book_court(self, user_name, contact, players, time_slot):

        # Validate player count
        if players <= 2:
            court_type = "Singles"
        elif players == 4:
            court_type = "Doubles"
        else:
            print("Invalid number of players!")
            return

        # Find available court
        for court in self.courts:
            if court.court_type == court_type and court.is_available(time_slot):
                booking = Booking(user_name, contact, players, court_type, time_slot)
                court.book(booking)
                booking.display_booking()
                return

        print(f"No {court_type} courts available at {time_slot}!")


# -------- Execution --------
center = BadmintonCenter()

center.book_court("Aggu", "9999999999", 2, "6AM-7AM")
center.book_court("Rahul", "8888888888", 2, "6AM-7AM")
center.book_court("Anil", "7777777777", 2, "6AM-7AM")  # Should fail
center.book_court("TeamX", "6666666666", 4, "6AM-7AM")