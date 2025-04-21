from datetime import datetime, date, timedelta
from typing import List

class Flight:
    """
    Represents a single flight option.
    """
    def __init__(
        self,
        flight_no: str,
        origin: str,
        dest: str,
        depart: datetime,
        arrive: datetime,
        price: float,
    ) -> None:
        self.flight_no = flight_no
        self.origin    = origin
        self.dest      = dest
        self.depart    = depart
        self.arrive    = arrive
        self.price     = price

    def duration(self) -> timedelta:
        """Return flight duration as a timedelta."""
        # — was missing a return statement
        return self.arrive - self.depart


class FlightRepository:
    """
    A simple in‑memory store of available flights.
    """
    def __init__(self) -> None:
        self._flights: List[Flight] = []

    def add_flight(self, flight: Flight) -> None:
        """Add a Flight to the repository."""
        self._flights.append(flight)

    def list_flights(self) -> List[Flight]:
        """Return all stored Flight objects."""
        # — fixed from `list.self._flights` to `list(self._flights)`
        return list(self._flights)


class FlightAggregator:
    """
    Core search logic over flights in a repository.
    """
    def __init__(self, repo: FlightRepository) -> None:
        self.repo = repo

    def search(
        self,
        origin: str,
        dest: str,
        travel_date: date,
        max_price: float = None
    ) -> List[Flight]:
        """
        Return flights matching origin → dest on travel_date.
        If max_price is provided, exclude more expensive options.
        """
        all_flights = self.repo.list_flights()

        matching = [
            flight                                             
            for flight in all_flights                          
            if flight.origin == origin
               and flight.dest == dest
               and flight.depart.date() == travel_date        # exact date match
               and (max_price is None or flight.price <= max_price)
        ]

        # sort cheapest first (in place)
        matching.sort(key=lambda flight: flight.price)
        return matching



# if __name__ == "__main__":
    
repo = FlightRepository()
repo.add_flight(Flight(
    "S123", "LHR", "CDG",
    datetime(2025, 5, 1, 9, 30),
    datetime(2025, 5, 1, 11, 0),
    120.50
))
repo.add_flight(Flight(
    "S124", "LHR", "CDG",
    datetime(2025, 5, 1, 15, 0),
    datetime(2025, 5, 1, 16, 30),
    95.00
))

agg = FlightAggregator(repo)

print("All flights on 2025‑05‑01:")
for f in agg.search("LHR", "CDG", date(2025, 5, 1)):
    print(f"{f.flight_no} @ £{f.price}")

print("\nBudget flights ≤ £100:")
for f in agg.search("LHR", "CDG", date(2025, 5, 1), max_price=100.0):
    print(f"{f.flight_no} @ £{f.price}")
