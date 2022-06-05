package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.model.Vehicle;

public interface RegisterService {

    User registerUser(User user);

    Driver registerDriver(Driver driver);

    Vehicle registerVehicle(Vehicle vehicle);
}
