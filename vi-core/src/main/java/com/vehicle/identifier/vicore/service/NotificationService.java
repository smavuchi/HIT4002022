package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.Notification;
import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;

public interface NotificationService {

    boolean sendNotification(Notification notification);

    void sendRegistrationEmail(Vehicle vehicle);

    void sendEmailNotification(Notification notification);
}
