package com.vehicle.identifier.vicore.service;

import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.repository.TimeLogRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.ZonedDateTime;
import java.util.List;
import java.util.Optional;

@Component
public class TimeLogServiceImpl implements TimeLogService{

    @Autowired
    TimeLogRepo timeLogRepo;

    @Override
    public TimeLog addEntry(TimeLog timeLog) {
        timeLogRepo.save(timeLog);
        return timeLog;
    }

    @Override
    public TimeLog addExit(String vehicleId, ZonedDateTime exitTime) {
        TimeLog timeLog = timeLogRepo.findByVehicleIdAndExitedNull(vehicleId);
        timeLog.setExited(exitTime);
        timeLogRepo.save(timeLog);
        return timeLog;

    }

    @Override
    public List<TimeLog> getAllCurrentLogs() {

        List<TimeLog> timeLogList = timeLogRepo.findAllByCreatedAfter(ZonedDateTime.now().minusDays(1));
        return timeLogList;
    }

    @Override
    public Optional<TimeLog> getTimeLogById(String timeLogId) {
        Optional<TimeLog> timeLog = timeLogRepo.findById(timeLogId);
        return timeLog;
    }

    @Override
    public void addTimeEntry(TimeLog timeLog) {
        timeLogRepo.save(timeLog);
    }
}
