package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.TimeLog;

import java.time.ZonedDateTime;
import java.util.List;
import java.util.Optional;

public interface TimeLogService {

    TimeLog addEntry(TimeLog timeLog);

    TimeLog addExit(String vehicleId, ZonedDateTime exitTime);

    List<TimeLog> getAllCurrentLogs();

    Optional<TimeLog> getTimeLogById(String timeLogId);

    void addTimeEntry(TimeLog timeLog);
}
