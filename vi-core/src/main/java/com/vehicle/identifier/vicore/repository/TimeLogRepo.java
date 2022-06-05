package com.vehicle.identifier.vicore.repository;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.TimeLog;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.ZonedDateTime;
import java.util.List;

public interface TimeLogRepo extends JpaRepository<TimeLog, String> {

    TimeLog findByVehicleIdAndExitedNull(String vehicleId);

    List<TimeLog> findAllByCreatedAfter(ZonedDateTime today);
}
