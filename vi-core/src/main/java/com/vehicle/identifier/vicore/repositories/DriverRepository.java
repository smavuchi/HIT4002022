package com.vehicle.identifier.vicore.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.vehicle.identifier.vicore.models.Driver;

@Repository
public interface DriverRepository extends JpaRepository<Driver, Integer> {

    Driver findById (String id);

}
