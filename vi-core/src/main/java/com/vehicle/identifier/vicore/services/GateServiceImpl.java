package com.vehicle.identifier.vicore.services;

import org.springframework.stereotype.Component;

@Component
public class GateServiceImpl implements GateService {

    @Override
    public boolean openGate() {
        return false;
    }
}
