package com.vehicle.identifier.vicore.services;
import com.vehicle.identifier.vicore.models.Setting;
import com.vehicle.identifier.vicore.repositories.SettingRepository;
import org.springframework.stereotype.Service;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;


@Service
public class SettingServiceImpl implements SettingService {

	private final SettingRepository repository;

	public SettingServiceImpl(SettingRepository repository) {

		this.repository = repository;
	}

	@Override
	public Setting putUpdatedValue(String key, String value) {
		Setting setting = repository.findSettingByKey(key);
		setting.setValue(value);
		setting.setUpdated(ZonedDateTime.now(ZoneId.of("Africa/Harare")));
		return repository.save(setting);
	}


	@Override
	public Setting getSettingByKey(String key) {

		return repository.findSettingByKey(key);
	}


	@Override
	public List<Setting> getAllSettings() {
		return repository.findAll();
	}


}
