from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "CDG"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
       flight.price
    except AttributeError:
        pass
    else:
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_notification(
                msg=f"Low price alert!\n"
                    f"Only {flight.price}€ to fly\n"
                    f"from: {flight.origin_city}-{flight.origin_airport}\n"
                    f"to: {flight.destination_city}-{flight.destination_airport}\n "
                    f"from: {flight.out_date} to: {flight.return_date}."
            )
