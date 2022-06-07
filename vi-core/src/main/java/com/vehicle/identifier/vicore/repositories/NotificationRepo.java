package com.vehicle.identifier.vicore.repositories;

import com.vehicle.identifier.vicore.models.Notification;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NotificationRepo extends JpaRepository<Notification, String> {
}
