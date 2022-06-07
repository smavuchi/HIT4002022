package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Timelog;
import com.vehicle.identifier.vicore.repositories.TimelogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.ZonedDateTime;
import java.util.List;

@Component
public class TimelogServiceImpl implements TimelogService{

    @Autowired
    TimelogRepository timelogRepository;

    ZonedDateTime dateNow = ZonedDateTime.now();

    @Override
    public List<Timelog> getTimelogs() {
        return timelogRepository.findAll();
    }

    @Override
    public List<Timelog> getTodaysTimelogs() {
        return timelogRepository.findAllByCreatedAfter(dateNow.minusDays(1));
    }

    @Override
    public List<Timelog> getLoggedInTimelogs() {
        ZonedDateTime dateNow = ZonedDateTime.now();
        return timelogRepository.findAllByCreatedAfterAndAndLoggedOut(dateNow.minusDays(1), null);
    }

    @Override
    public Timelog findById(String id) {
        return timelogRepository.findById(id);
    }

    @Override
    public void addTimeEntry(Timelog timelog) {
        timelogRepository.save(timelog);
    }

    @Override
    public List<Timelog> getTimelogByLicensePlace(String licensePlate) {
        return timelogRepository.findTimelogByVehicleId(licensePlate);
    }

    @Override
    public void save(Timelog timelog1) {

         timelogRepository.save(timelog1);
    }
}
