package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.repository.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

@Component
public class UserServiceImpl implements UserService{

    @Autowired
    UserRepo userRepo;

    @Override
    public Optional<User> findUserById(String userId) {
        Optional<User> user = userRepo.findById(userId);
        return user;
    }

    @Override
    public List<User> findAllUsers() {
        List<User> users = userRepo.findAll();
        return users;
    }

    @Override
    public User putUser(User user) {
        return null;
    }

    @Override
    public User updateUser(User user) {
        return null;
    }

    @Override
    public void deleteUser(String userId) {
        userRepo.deleteById(userId);
    }
}
