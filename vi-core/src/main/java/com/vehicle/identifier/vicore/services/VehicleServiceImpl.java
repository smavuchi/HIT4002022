package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Driver;
import com.vehicle.identifier.vicore.models.Vehicle;
import com.vehicle.identifier.vicore.repositories.VehicleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

import static com.vehicle.identifier.vicore.util.Util.currentTime;
import static com.vehicle.identifier.vicore.util.Util.uuid;

@Component
public class VehicleServiceImpl implements VehicleService{

    @Autowired
    private VehicleRepository vehicleRepository;

    @Override
    public List<Vehicle> getVehicles() {
        return vehicleRepository.findAll();
    }

    @Override
    public void save(Vehicle vehicle) {
        vehicleRepository.save(vehicle);
    }

    @Override
    public Vehicle findById(String id) {
        return vehicleRepository.findById(id);
    }

    @Override
    public void delete(Integer id) {
        vehicleRepository.deleteById(id);
    }

    @Override
    public Vehicle getVehicleByLicensePlate(String licensePlate) {
        return vehicleRepository.findByLicensePlate(licensePlate);
    }

    @Override
    public void addFromRemoteVehicle(Vehicle vehicle) {
        vehicle.setId(uuid());
        vehicle.setStatus("LOGGED_IN");
        vehicle.setCreated(currentTime());
        vehicle.setUpdated(currentTime());
        vehicleRepository.save(vehicle);
    }

    @Override
    public void blacklist(Vehicle vehicle) {
        vehicleRepository.save(vehicle);
    }

    @Override
    public void update(Driver driver) {
        Vehicle  vehicle=   vehicleRepository.findById(driver.getVehicleId());
        vehicle.setDriverId(driver.getId());
        vehicleRepository.save(vehicle);


    }
}
