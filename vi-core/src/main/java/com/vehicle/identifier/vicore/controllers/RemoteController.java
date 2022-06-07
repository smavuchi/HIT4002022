package com.vehicle.identifier.vicore.controllers;

import com.vehicle.identifier.vicore.models.*;
import com.vehicle.identifier.vicore.services.*;
import com.vehicle.identifier.vicore.util.Util;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.List;

import static com.vehicle.identifier.vicore.util.Notifications.*;
import static com.vehicle.identifier.vicore.util.Times.entryTime;

@Controller
public class RemoteController {

    private static final String MAIN_ENTRANCE_CAMERA = "MAIN_ENTRANCE_CAMERA";
    private static final String MAIN_EXIT_CAMERA = "MAIN_EXIT_CAMERA";
    @Autowired
    VehicleService vehicleService;

    @Autowired
    GateService gateService;

    @Autowired
    NotificationService notificationService;

    @Autowired
    DriverService driverService;

    @Autowired
    SettingService settingService;

    @Autowired
    TimelogService timelogService;

    @RequestMapping(method = RequestMethod.POST, value = "/remote",
            consumes = "application/json", produces = "application/json")
    public ResponseEntity getVehicleFromRemote(@RequestBody Vehicle vehicle) {

        Setting mainEntrance = settingService.getSettingByKey(MAIN_ENTRANCE_CAMERA);


        if (Boolean.parseBoolean(mainEntrance.getValue())) {

            Vehicle dbLookUpVehicle = vehicleService.getVehicleByLicensePlate(vehicle.getLicensePlate());
            Timelog timelog = entryTime(vehicle.getLicensePlate());
            timelogService.addTimeEntry(timelog);

            if (dbLookUpVehicle != null && dbLookUpVehicle.blacklisted) {

                Notification notification = blockedNotification(timelog);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);
            }


            if (!checkIfVehicleExists(vehicle.getLicensePlate())) {
                vehicleService.addFromRemoteVehicle(vehicle);
                gateService.openGate();
                System.out.println("Vehicle Saved");
                timelogService.addTimeEntry(entryTime(vehicle.getLicensePlate()));
                System.out.println("Time Saved");
                notificationService.sendRegistrationEmail(vehicle);
                return ResponseEntity.ok().build();
            }
            if ("LOGGED_IN".equalsIgnoreCase(dbLookUpVehicle.getStatus())) {

                Notification notification = investigateIncorrectEntry(timelog,dbLookUpVehicle);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);

                return ResponseEntity.ok().build();


            }



            if(dbLookUpVehicle.getDriverId() == null ||
            dbLookUpVehicle.getDriverId().isEmpty()){

                Notification notification = unverifiedDriver(timelog,dbLookUpVehicle);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);

                return ResponseEntity.ok().build();

            }
            Driver driver = driverService.findById(dbLookUpVehicle.getDriverId());
            gateService.openGate();

            dbLookUpVehicle.setStatus("LOGGED_IN");
            vehicleService.save(dbLookUpVehicle);

            Notification notification = arrivalNotification(timelog, driver);
            System.out.println("Sending email");
            notificationService.sendEmailNotification(notification);

            return ResponseEntity.ok().build();

        }

        Setting mainExit = settingService.getSettingByKey(MAIN_EXIT_CAMERA);

        if (Boolean.parseBoolean(mainExit.getValue())) {

            Vehicle dbLookUpVehicle = vehicleService.getVehicleByLicensePlate(vehicle.getLicensePlate());
            Timelog timelog = entryTime(vehicle.getLicensePlate());


            if (dbLookUpVehicle != null && dbLookUpVehicle.blacklisted) {

                Notification notification = blockedVehicleExitNotification(timelog);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);
            }


            if ("LOGGED_OUT".equalsIgnoreCase(dbLookUpVehicle.getStatus())) {

                Notification notification = investigateIncorrectExit(timelog,dbLookUpVehicle);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);

                return ResponseEntity.ok().build();


            }

            List<Timelog> timelogList = timelogService.getTimelogByLicensePlace(dbLookUpVehicle.getLicensePlate());

            timelogList.forEach(timelog1 -> {

                timelog1.setLoggedOut(Util.currentTime());
                timelogService.save(timelog1);
            });

            dbLookUpVehicle.setStatus("LOGGED_OUT");
            vehicleService.save(dbLookUpVehicle);
            Driver driver = driverService.findById(dbLookUpVehicle.getDriverId());
            gateService.openGate();
            if( driver != null && driver.getEmail() != null ) {

                Notification notification = departureNotification(timelog, driver);
                System.out.println("Sending email");
                notificationService.sendEmailNotification(notification);
            }

            return ResponseEntity.ok().build();

        }

        return null;
    }

    public boolean checkIfVehicleExists(String licencePlate) {
        Vehicle vehicle = vehicleService.getVehicleByLicensePlate(licencePlate);
        if (vehicle == null || vehicle.getId().isEmpty() || vehicle.getId() == null) {
            return false;
        }
        return true;
    }
}
