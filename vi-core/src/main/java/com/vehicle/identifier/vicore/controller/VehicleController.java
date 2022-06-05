package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.service.VehicleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@RestController
@RequestMapping("/vehicle")
public class VehicleController {

    @Autowired
    VehicleService vehicleService;

    @RequestMapping(method = RequestMethod.GET, value = "/{licensePlate}")
    public ModelAndView getVehicleByLicensePlate(@PathVariable("licensePlate") String licensePlate){
        ModelAndView modelAndView = new ModelAndView("vehicle/view");
        Vehicle vehicles = vehicleService.getVehicleByLicensePlate(licensePlate);
        modelAndView.addObject(vehicles);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/all")
    public ModelAndView getVehicles(){
        ModelAndView modelAndView = new ModelAndView("vehicle/list");
        List<Vehicle> vehicles = vehicleService.getAllVehicles();
        modelAndView.addObject(vehicles);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/delete/{vehicleId}")
    public ModelAndView deleteVehicle(@PathVariable("vehicleId") String vehicleId){
        vehicleService.deleteVehicle(vehicleId);
        return null;
    }
}
