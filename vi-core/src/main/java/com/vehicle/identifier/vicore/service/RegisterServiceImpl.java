package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Auth;
import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.repository.AuthRepo;
import com.vehicle.identifier.vicore.repository.DriverRepo;
import com.vehicle.identifier.vicore.repository.UserRepo;
import com.vehicle.identifier.vicore.repository.VehicleRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import static com.vehicle.identifier.vicore.util.Util.currentTime;
import static com.vehicle.identifier.vicore.util.Util.uuid;

@Component
public class RegisterServiceImpl implements RegisterService {

    @Autowired
    AuthRepo authRepo;

    @Autowired
    DriverRepo driverRepo;

    @Autowired
    UserRepo userRepo;

    @Autowired
    VehicleRepo vehicleRepo;

    @Override
    public User registerUser(User user) {
        user.setId(uuid());
        user.setCreated(currentTime());
        user.setUpdated(currentTime());
        userRepo.save(user);

        Auth auth = new Auth();
        auth.setCreated(user.getCreated());
        auth.setUpdated(user.getUpdated());
        auth.setId(uuid());
        auth.setUserId(user.getUsername());
        auth.setPassword("12345678");
        authRepo.save(auth);
        return user;
    }

    @Override
    public Driver registerDriver(Driver driver) {
        driver.setId(uuid());
        driver.setCreated(currentTime());
        driver.setUpdated(currentTime());
        driverRepo.save(driver);
        return driver;
    }

    @Override
    public Vehicle registerVehicle(Vehicle vehicle) {
        vehicle.setId(uuid());
        vehicle.setCreated(currentTime());
        vehicle.setUpdated(currentTime());
        vehicleRepo.save(vehicle);
        return null;
    }
}
