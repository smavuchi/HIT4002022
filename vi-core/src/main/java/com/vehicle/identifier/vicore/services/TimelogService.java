package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Timelog;

import java.util.List;

public interface TimelogService {
    List<Timelog> getTimelogs();

    List<Timelog> getTodaysTimelogs();

    List<Timelog> getLoggedInTimelogs();

    Timelog findById(String id);

    void addTimeEntry(Timelog timelog);

    List<Timelog> getTimelogByLicensePlace(String licensePlate);

    void save(Timelog timelog1);
}
