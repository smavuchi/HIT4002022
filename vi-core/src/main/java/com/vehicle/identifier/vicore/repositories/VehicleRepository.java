package com.vehicle.identifier.vicore.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.vehicle.identifier.vicore.models.Vehicle;

@Repository
public interface VehicleRepository extends JpaRepository<Vehicle, Integer> {

    Vehicle findByLicensePlate(String licensePlate);

    Vehicle findById(String id);
}
