package com.vehicle.identifier.vicore.repositories;

import com.vehicle.identifier.vicore.models.Notification;
import com.vehicle.identifier.vicore.models.Setting;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface SettingRepository extends JpaRepository<Setting, Integer> {


		Setting findSettingByKey(String key);
}
