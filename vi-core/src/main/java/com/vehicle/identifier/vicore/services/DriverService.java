package com.vehicle.identifier.vicore.services;

import java.util.List;

import com.vehicle.identifier.vicore.models.Driver;

public interface DriverService {

	List<Driver> getDrivers();
	
	void save(Driver driver);
	
	Driver findById(String id);

	void delete(Integer id);
}
