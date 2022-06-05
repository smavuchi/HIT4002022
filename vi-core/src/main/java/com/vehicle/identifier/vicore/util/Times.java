package com.vehicle.identifier.vicore.util;

import com.vehicle.identifier.vicore.model.TimeLog;

import static com.vehicle.identifier.vicore.util.Util.currentTime;
import static com.vehicle.identifier.vicore.util.Util.uuid;

public class Times {

    public static TimeLog entryTime(String vehicleId){
        TimeLog timeLog = new TimeLog();
        timeLog.setId(uuid());
        timeLog.setCreated(currentTime());
        timeLog.setUpdated(currentTime());
        timeLog.setEntered(currentTime());
        timeLog.setVehicleId(vehicleId);
        return timeLog;
    }
}
