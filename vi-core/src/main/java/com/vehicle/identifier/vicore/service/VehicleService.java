package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;

import java.util.List;
import java.util.Optional;

public interface VehicleService {

    Optional<Vehicle> getVehicleById(String vehicleId);

    List<Vehicle> getAllVehicles();

    List<Vehicle> findAllVehiclesByDriver(String driverId);

    Vehicle putVehicle(Vehicle vehicle);

    Vehicle updateVehicle(Vehicle vehicle);

    Vehicle getVehicleByLicensePlate(String licensePlate);

    Vehicle deleteVehicle(String vehicleId);

    void addFromRemoteVehicle(Vehicle vehicle);
}
