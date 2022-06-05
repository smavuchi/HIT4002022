package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.User;

public interface AuthService {

    User login(String userId, String password);

    boolean forgotPassword(String userId, String email);
}
