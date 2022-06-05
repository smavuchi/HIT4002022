package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.Notification;
import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.service.*;
import org.apache.catalina.connector.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import static com.vehicle.identifier.vicore.util.Notifications.arrivalNotification;
import static com.vehicle.identifier.vicore.util.Times.entryTime;

@RestController
@RequestMapping( value = "/remote")
public class RemoteController {

    @Autowired
    VehicleService vehicleService;

    @Autowired
    GateService gateService;

    @Autowired
    NotificationService notificationService;

    @Autowired
    DriverService driverService;

    @Autowired
    TimeLogService timeLogService;

    @RequestMapping(method = RequestMethod.POST, value = "/vehicle",
            consumes = "application/json", produces = "application/json")
    public int getVehicleFromRemote(@RequestBody Vehicle vehicle){
        if(!checkIfVehicleExists(vehicle.getLicensePlate())){
            gateService.openGate();
            vehicleService.addFromRemoteVehicle(vehicle);
            System.out.println("Vehicle Saved");
            timeLogService.addTimeEntry(entryTime(vehicle.getLicensePlate()));
            System.out.println("Time Saved");
            notificationService.sendRegistrationEmail(vehicle);
            return Response.SC_OK;
        }
        Vehicle vehicle1 = vehicleService.getVehicleByLicensePlate(vehicle.getLicensePlate());
        Driver driver = driverService.findDriverById(vehicle1.getDriverId());
        gateService.openGate();
        TimeLog timeLog = entryTime(vehicle.getLicensePlate());
        timeLogService.addTimeEntry(timeLog);
        Notification notification = arrivalNotification(timeLog, driver);

//        notificationService.sendWaNotification(notification);
        System.out.println("Sending email");
        notificationService.sendEmailNotification(notification);

        return Response.SC_OK;
    }

    public boolean checkIfVehicleExists(String licencePlate){
        Vehicle vehicle = vehicleService.getVehicleByLicensePlate(licencePlate);
        if(vehicle == null || vehicle.getId().isEmpty() || vehicle.getId() == null){
            return false;
        }
        return true;
    }
}
