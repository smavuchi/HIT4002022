package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Notification;
import com.vehicle.identifier.vicore.models.Vehicle;

public interface NotificationService {

    boolean sendNotification(Notification notification);

    void sendRegistrationEmail(Vehicle vehicle);

    void sendEmailNotification(Notification notification);
}
