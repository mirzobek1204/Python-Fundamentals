def book_stay(guests_db, room_catalog, guest_id, room_type, nights):

    if guest_id not in guests_db:
        raise KeyError("Guest ID not found")
    if room_type not in room_catalog:
        raise KeyError("Invalid room type")
    if type(nights) is not int or nights<1:
        raise ValueError("Nights must be positive integer")
    room_price=room_catalog[room_type]["price"]
    total_cost=(nights*room_price)+room_catalog[room_type]["cleaning_fee"]
    balance=guests_db[guest_id]["balance"]
    if balance<total_cost:
        raise ValueError("Insufficient funds")
    guests_db[guest_id]["balance"]-=total_cost
    return total_cost
def process_bookings(guests_db,room_catalog,booking_queue):
    total_revenue=0
    failed_bookings=0
    for guest_id ,room_type,nights in booking_queue:
        try:
            cost=book_stay(guests_db, room_catalog,guest_id, room_type, nights)
            total_revenue+=cost
        except (KeyError, ValueError) as e:
          print(f"Booking Error for {guest_id}: {e}")
          failed_bookings+=1
    return {'total_revenue': total_revenue, 'failed_bookings': failed_bookings}
rooms = {
    "Standard": {"price": 100.0, "cleaning_fee": 20.0},
    "Suite":    {"price": 200.0, "cleaning_fee": 50.0}
}

guests = {
    "G1": {"balance": 300.0},
    "G2": {"balance": 50.0}
}

bookings = [
    ("G1", "Standard", 2),   
    ("G2", "Suite", 1),       
    ("G3", "Standard", 1),    
    ("G1", "Penthouse", 1),  
    ("G1", "Standard", 0)     
]
print(process_bookings(guests,rooms,bookings))

    
    
