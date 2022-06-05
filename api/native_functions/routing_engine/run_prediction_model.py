import pickle
import numpy as np
from datetime import datetime

def run_prediction_model(prediction_day, prediction_time, pickup_station, dropoff_station):
    # NDICHATANGIRA PANO, Internet yacho yarova pasi ndingazviitewo sei :(

    # day_time = datetime.now()
    # day_time = day_time.strftime("%H:%M")
    day_time = prediction_time

    hours, minutes = day_time.split(":")

    day_time_minutes = (int(hours) * 60) + int(minutes)

    # CHECKING GREETINGS
    # Morning
    morning_start = "05:00"
    hours, minutes = morning_start.split(":")
    morning_start_dtm = (int(hours) * 60) + int(minutes)

    morning_end = "11:59"
    hours, minutes = morning_end.split(":")
    morning_end_dtm = (int(hours) * 60) + int(minutes)

    # Afternoon
    afternoon_start = "12:00"
    hours, minutes = afternoon_start.split(":")
    afternoon_start_dtm = (int(hours) * 60) + int(minutes)
    
    afternoon_end = "16:59"
    hours, minutes = afternoon_end.split(":")
    afternoon_end_dtm = (int(hours) * 60) + int(minutes)


    # Evening
    evening_start = "17:00"
    hours, minutes = evening_start.split(":")
    evening_start_dtm = (int(hours) * 60) + int(minutes)

    evening_end = "22:59"
    hours, minutes = evening_end.split(":")
    evening_end_dtm = (int(hours) * 60) + int(minutes)

    # Midnight
    midnight_start = "23:00"
    midnight_two_start = "00:00"
    hours, minutes = midnight_start.split(":")
    hours_two, minutes_two = midnight_two_start.split(":")
    midnight_start_dtm = (int(hours) * 60) + int(minutes)
    midnight_two_start_dtm = (int(hours_two) * 60) + int(minutes_two)

    midnight_end = "04:59"
    hours, minutes = midnight_end.split(":")
    midnight_end_dtm = (int(hours) * 60) + int(minutes)

    if day_time_minutes >= morning_start_dtm and day_time_minutes <= morning_end_dtm:
        greetings_Morning = 1
        greetings_Afternoon = 0
        greetings_Evening = 0
        greetings_Midnight = 0

    elif day_time_minutes >= afternoon_start_dtm and day_time_minutes <= afternoon_end_dtm:
        greetings_Morning = 0
        greetings_Afternoon = 1
        greetings_Evening = 0
        greetings_Midnight = 0

    elif day_time_minutes >= evening_start_dtm and day_time_minutes <= evening_end_dtm:
        greetings_Morning = 0
        greetings_Afternoon = 0
        greetings_Evening = 1
        greetings_Midnight = 0

    elif day_time_minutes >= day_time_minutes >= midnight_two_start_dtm or midnight_start_dtm and day_time_minutes <= midnight_end_dtm:
        greetings_Morning = 0
        greetings_Afternoon = 0
        greetings_Evening = 0
        greetings_Midnight = 1

    # if station_name != "City":
        
    # TESTING MODEL
    # departure_time = datetime.now()
    # departure_time = datetime.timestamp(departure_time)
    
    # pickup_station = station_name
    # dropoff_station = "City"
    public_holiday = 0
    
    # day_time_minutes = 560

    weekend = 0

    # greetings_Afternoon = 1
    # greetings_Evening = 0
    # greetings_Morning = 0

    day_Friday = 0
    day_Monday = 0
    day_Saturday = 0
    day_Sunday = 0
    day_Thursday = 0
    day_Tuesday = 0
    day_Wednesday = 0

    if prediction_day == "Sunday":
        day_Sunday = 1
        weekend = 1

    elif prediction_day == "Monday":
        day_Monday = 1
        weekend = 0

    elif prediction_day == "Tuesday":
        day_Tuesday = 1
        weekend = 0

    elif prediction_day == "Wednesday":
        day_Wednesday = 1
        weekend = 0

    elif prediction_day == "Thursday":
        day_Thursday = 1
        weekend = 0

    elif prediction_day == "Friday":
        day_Friday = 1
        weekend = 0

    elif prediction_day == "Saturday":
        day_Saturday = 1
        weekend = 1

    prediction_input = []
    prediction_input.append(weekend)
    prediction_input.append(day_time_minutes)
    prediction_input.append(greetings_Afternoon)
    prediction_input.append(greetings_Evening)
    prediction_input.append(greetings_Midnight)
    prediction_input.append(greetings_Morning)
    prediction_input.append(day_Friday)
    prediction_input.append(day_Monday)
    prediction_input.append(day_Saturday)
    prediction_input.append(day_Sunday)
    prediction_input.append(day_Thursday)
    prediction_input.append(day_Tuesday)
    prediction_input.append(day_Wednesday)
    
    # pickup station
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)

    # dropoff station
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)
    prediction_input.append(0)

    # Pickup
    if pickup_station == "Belvedere":
        prediction_input[13] = 1

    elif pickup_station == "City":
        prediction_input[14] = 1

    elif pickup_station == "Dzivarasekwa":
        prediction_input[15] = 1

    elif pickup_station == "Kuwadzana":
        prediction_input[16] = 1

    elif pickup_station == "Mabelreign":
        prediction_input[17] = 1

    elif pickup_station == "Marlborough":
        prediction_input[18] = 1

    elif pickup_station == "Mount Pleasant":
        prediction_input[19] = 1

    elif pickup_station == "Vainona":
        prediction_input[20] = 1

    elif pickup_station == "Warren Park":
        prediction_input[21] = 1

    elif pickup_station == "Westgate":
        prediction_input[22] = 1


    # Drop off
    if dropoff_station == "Belvedere":
        prediction_input[23] = 1

    elif dropoff_station == "City":
        prediction_input[24] = 1

    elif dropoff_station == "Dzivarasekwa":
        prediction_input[25] = 1

    elif dropoff_station == "Kuwadzana":
        prediction_input[26] = 1

    elif dropoff_station == "Mabelreign":
        prediction_input[27] = 1

    elif dropoff_station == "Marlborough":
        prediction_input[28] = 1

    elif dropoff_station == "Mount Pleasant":
        prediction_input[29] = 1

    elif dropoff_station == "Vainona":
        prediction_input[30] = 1

    elif dropoff_station == "Warren Park":
        prediction_input[31] = 1

    elif dropoff_station == "Westgate":
        prediction_input[32] = 1

    prediction_input = [prediction_input]

    prediction_input = np.array(prediction_input)

    # print("~~~~")
    # print(prediction_input)
    # print("~~~~")

    pickle_in = open("files/new/waybillmodel.pickle", "rb")
    waybill_model = pickle.load(pickle_in)

    prediction = waybill_model.predict(prediction_input)
    prediction = int(prediction[0])

    if prediction < 0:
        prediction = 0

    prediction = {
        "prediction_count": prediction,
        "pickup_station": pickup_station,
        "dropoff_station": dropoff_station,
    }
    # print("####")

    return prediction

    # else:
    #     prediction = 0
    #     return prediction