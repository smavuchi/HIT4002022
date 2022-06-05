package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.Notification;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NotificationRepo extends JpaRepository<Notification, String> {
}
