package com.vehicle.identifier.vicore.repositories;

import com.vehicle.identifier.vicore.models.Timelog;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.ZonedDateTime;
import java.util.List;

public interface TimelogRepository extends JpaRepository<Timelog, Integer> {

    List<Timelog> findAllByCreatedAfter(ZonedDateTime dateNow);

    List<Timelog> findAllByCreatedAfterAndAndLoggedOut(ZonedDateTime in, ZonedDateTime out);

    Timelog findById(String id);

    List<Timelog> findTimelogByLicensePlate(String licensePlate);

    List<Timelog> findTimelogByVehicleId(String vehicleId);


}
