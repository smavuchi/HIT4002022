package com.vehicle.identifier.vicore.util;

import com.vehicle.identifier.vicore.models.Timelog;

public class Times {

    public static Timelog entryTime(String vehicleId){
        Timelog timeLog = new Timelog();
        timeLog.setId(Util.uuid());
        timeLog.setCreated(Util.currentTime());
        timeLog.setUpdated(Util.currentTime());
        timeLog.setLoggedIn(Util.currentTime());
        timeLog.setVehicleId(vehicleId);
        return timeLog;
    }
}
