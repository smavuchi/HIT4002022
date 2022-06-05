import pickle
import numpy as np
from datetime import datetime

def station_prediction(prediction_input, station_name):
    # NDICHATANGIRA PANO, Internet yacho yarova pasi ndingazviitewo sei :(

    day_time = datetime.now()
    day_time = day_time.strftime("%H:%M")

    hours, minutes = day_time.split(":")

    day_time_minutes = (int(hours) * 60) + int(minutes)

    if station_name != "City":
        # TESTING MODEL
        departure_time = datetime.now()
        departure_time = datetime.timestamp(departure_time)
        
        pickup_station = station_name
        dropoff_station = "City"
        public_holiday = 0
        weekend = 0
        # day_time_minutes = 560
        greetings_Afternoon = 1
        greetings_Evening = 0
        greetings_Morning = 0
        day_Friday = 0
        day_Monday = 0
        day_Saturday = 0
        day_Sunday = 0
        day_Thursday = 0
        day_Tuesday = 0
        day_Wednesday = 1

        prediction_input = []
        prediction_input.append(public_holiday)
        prediction_input.append(weekend)
        prediction_input.append(day_time_minutes)
        prediction_input.append(greetings_Afternoon)
        prediction_input.append(greetings_Evening)
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
        # print("####")
        # print(prediction)

        if prediction < 0:
            print(prediction)
            prediction = 0

        return prediction

    else:
        prediction = 0
        return prediction