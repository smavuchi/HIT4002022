package com.vehicle.identifier.vicore.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.vehicle.identifier.vicore.models.Country;

@Repository

public interface CountryRepository extends JpaRepository<Country, Integer> {

}
