package com.vehicle.identifier.vicore.services;

import java.util.List;

import com.vehicle.identifier.vicore.models.Driver;
import com.vehicle.identifier.vicore.models.Vehicle;

public interface VehicleService {
	
	List<Vehicle> getVehicles();
	
	void save(Vehicle vehicle);
	
	Vehicle findById(String id);

	void delete(Integer id);

	Vehicle getVehicleByLicensePlate(String licensePlate);

	void addFromRemoteVehicle(Vehicle vehicle);

	void blacklist(Vehicle vehicleId);

	void update(Driver driver);

}
