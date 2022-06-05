package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Auth;
import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.repository.AuthRepo;
import com.vehicle.identifier.vicore.repository.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class AuthServiceImpl implements AuthService{

    @Autowired
    AuthRepo authRepo;

    @Autowired
    UserRepo userRepo;

    @Override
    public User login(String userId, String password) {
        Auth auth = authRepo.findByUserId(userId);
        System.out.println("Auth" + auth.getUserId());
        if(auth == null || !auth.getPassword().equals(password)){
            User user = new User();
            return user;
        }
        User user = userRepo.findUserByUsername(auth.getUserId());
        System.out.println("user" + user.getUsername());
        return user;
    }

    @Override
    public boolean forgotPassword(String userId, String email) {
        User user = userRepo.getById(userId);
        if(!user.getEmail().equals(email)){
            return false;
        }
        return true;
    }
}
