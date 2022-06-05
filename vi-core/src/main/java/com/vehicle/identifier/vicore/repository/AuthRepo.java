package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.Auth;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AuthRepo extends JpaRepository<Auth, String> {

    Auth findByUserId(String userId);
}
