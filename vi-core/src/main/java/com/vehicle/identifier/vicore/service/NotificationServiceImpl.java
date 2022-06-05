package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Notification;
import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.repository.NotificationRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Properties;

import static com.vehicle.identifier.vicore.util.Notifications.registrationNotification;

@Component
public class NotificationServiceImpl implements NotificationService{

    @Autowired
    NotificationRepo notificationRepo;

    @Override
    public boolean sendNotification(Notification notification) {
        notificationRepo.save(notification);

        return false;
    }

    @Override
    public void sendRegistrationEmail(Vehicle vehicle) {
        Notification notification = registrationNotification(vehicle);

    }

    @Override
    public void sendEmailNotification(Notification notification) {
    }
}
