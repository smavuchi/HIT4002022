package com.vehicle.identifier.vicore.services;

import com.vehicle.identifier.vicore.models.Setting;

import java.util.List;

public interface SettingService {

    Setting putUpdatedValue(String key, String value);

    Setting getSettingByKey(String key);

    List<Setting> getAllSettings();
}
