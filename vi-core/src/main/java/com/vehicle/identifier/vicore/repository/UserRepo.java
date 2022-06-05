package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepo extends JpaRepository<User, String> {

    User findUserByUsername(String username);
}
