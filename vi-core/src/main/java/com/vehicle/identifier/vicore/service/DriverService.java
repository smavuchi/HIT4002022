package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Driver;

import java.util.List;

public interface DriverService {

    Driver findDriverById(String driverId);

    List<Driver> getAllDrivers();

    void deleteDriver(String driverId);

    boolean putDriver(Driver driver);

    boolean updateDriver(Driver driver);
}
