#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Reconstruct your trip from your mass of flight tickets. Each ticket is
    represented as a class.

    The source string represents the starting airport and the destination string
    represents the next airport along our trip. The ticket for your first flight
    has a destination with a source of NONE, and the ticket for your final flight
    has a source with a destination of NONE.

    Pseudocode for an array of Tickets might look like this:

    tickets = [
        Ticket{ source: "PIT", destination: "ORD" },
        Ticket{ source: "XNA", destination: "CID" },
        Ticket{ source: "SFO", destination: "BHM" },
        Ticket{ source: "FLG", destination: "XNA" },
        Ticket{ source: "NONE", destination: "LAX" },
        Ticket{ source: "LAX", destination: "SFO" },
        Ticket{ source: "CID", destination: "SLC" },
        Ticket{ source: "ORD", destination: "NONE" },
        Ticket{ source: "SLC", destination: "PIT" },
        Ticket{ source: "BHM", destination: "FLG" }
    ]

    Your function should output an array of strings with the entire route of your trip.
    For the above example, it should look like this:

    ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
    Your solution should run in linear time. You can assume that your function will
    always be handed a valid ticket chain as input.
    """
    # Your code here

    # caching again
    cache = {}

    # create array with slots, similar to ht implementation
    route = [None] * length

    # iterate over the length to catch all tickets and store them
    for t in tickets:
        cache[t.source] = t.destination

    # Define first flight per rules
    first_flight = cache["NONE"]

    # now add to each stop
    for f in range(length):
        route[f] = first_flight
        first_flight = cache[first_flight]

    return route
