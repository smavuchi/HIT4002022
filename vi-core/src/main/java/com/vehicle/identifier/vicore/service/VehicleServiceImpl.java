package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.repository.VehicleRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

import static com.vehicle.identifier.vicore.util.Util.currentTime;
import static com.vehicle.identifier.vicore.util.Util.uuid;

@Component
public class VehicleServiceImpl implements VehicleService{

    @Autowired
    VehicleRepo vehicleRepo;

    @Override
    public Optional<Vehicle> getVehicleById(String vehicleId) {
        Optional<Vehicle> vehicle = vehicleRepo.findById(vehicleId);
        return vehicle;
    }

    @Override
    public List<Vehicle> getAllVehicles() {
        List<Vehicle> vehicles = vehicleRepo.findAll();
        return vehicles;
    }

    @Override
    public List<Vehicle> findAllVehiclesByDriver(String driverId) {
        List<Vehicle> vehicles = vehicleRepo.findAllByDriverId(driverId);
        return vehicles;
    }

    @Override
    public Vehicle putVehicle(Vehicle vehicle) {
        return null;
    }

    @Override
    public Vehicle updateVehicle(Vehicle vehicle) {
        return null;
    }

    @Override
    public Vehicle getVehicleByLicensePlate(String licensePlate) {
        Vehicle vehicle = vehicleRepo.getVehicleByLicensePlate(licensePlate);
        return vehicle;
    }

    @Override
    public Vehicle deleteVehicle(String vehicleId) {
        vehicleRepo.deleteById(vehicleId);
        return null;
    }

    @Override
    public void addFromRemoteVehicle(Vehicle vehicle) {
        vehicle.setId(uuid());
        vehicle.setCreated(currentTime());
        vehicle.setUpdated(currentTime());
        vehicleRepo.save(vehicle);
    }

}
