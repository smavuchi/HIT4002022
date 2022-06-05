package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.User;

import java.util.List;
import java.util.Optional;

public interface UserService {

    public Optional<User> findUserById(String userId);

    public List<User> findAllUsers();

    public User putUser(User user);

    public User updateUser(User user);

    public void deleteUser(String userId);
}
