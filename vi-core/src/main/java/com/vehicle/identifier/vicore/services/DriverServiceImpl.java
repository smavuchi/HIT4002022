package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Driver;
import com.vehicle.identifier.vicore.repositories.DriverRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class DriverServiceImpl implements DriverService{

    @Autowired
    DriverRepository driverRepository;

    @Override
    public List<Driver> getDrivers() {
        return driverRepository.findAll();
    }

    @Override
    public void save(Driver driver) {
        driverRepository.save(driver);
    }

    @Override
    public Driver findById(String id) {
        return driverRepository.findById(id);
    }

    @Override
    public void delete(Integer id) {
        driverRepository.deleteById(id);
    }
}
