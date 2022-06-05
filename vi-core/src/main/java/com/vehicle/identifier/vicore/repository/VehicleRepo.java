package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.service.VehicleService;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface VehicleRepo extends JpaRepository<Vehicle, String> {

    List<Vehicle> findAllByDriverId(String driverId);

    Vehicle getVehicleByLicensePlate(String licensePlate);
}
