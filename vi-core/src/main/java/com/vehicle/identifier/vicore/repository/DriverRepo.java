package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.Auth;
import com.vehicle.identifier.vicore.model.Driver;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DriverRepo extends JpaRepository<Driver, String> {
}
