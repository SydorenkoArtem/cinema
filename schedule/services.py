from schedule.models import Ticket


def get_free_places_in_hall(schedule):
    """Get Free places in schedule"""
    schedule_tickets = Ticket.objects.filter(schedule=schedule)
    place_count = 0
    for ticket in schedule_tickets:
        place_count += ticket.quantity
    free_places = schedule.hall.place - place_count
    return free_places


