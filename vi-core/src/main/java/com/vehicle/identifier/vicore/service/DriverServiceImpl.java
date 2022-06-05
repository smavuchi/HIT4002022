package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.repository.DriverRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class DriverServiceImpl implements DriverService{

    @Autowired
    DriverRepo driverRepo;

    @Override
    public Driver findDriverById(String driverId) {
        Driver driver = driverRepo.getById(driverId);
        return driver;
    }

    @Override
    public List<Driver> getAllDrivers() {
        List<Driver> drivers = driverRepo.findAll();
        return drivers;
    }

    @Override
    public void deleteDriver(String driverId) {
        driverRepo.deleteById(driverId);
    }

    @Override
    public boolean putDriver(Driver driver) {
        driverRepo.save(driver);
        return true;
    }

    @Override
    public boolean updateDriver(Driver driver) {
        driverRepo.existsById(driver.getId());
        return true;
    }
}
