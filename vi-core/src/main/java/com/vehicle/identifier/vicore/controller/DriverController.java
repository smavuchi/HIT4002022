package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.service.DriverService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/driver")
public class DriverController {

    @Autowired
    DriverService driverService;

    @RequestMapping(method = RequestMethod.POST, value = "/{driverId}")
    public ModelAndView getDriver(@RequestParam("driverId") String driverId){
        Driver driver = driverService.findDriverById(driverId);
        ModelAndView modelAndView = new ModelAndView("/driver/view");
        modelAndView.addObject(driver);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/all")
    public ModelAndView getAllDrivers(){
        ModelAndView modelAndView = new ModelAndView("driver/list");
        List<Driver> drivers = driverService.getAllDrivers();
        modelAndView.addObject(drivers);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/delete/{deleteId}")
    public ModelAndView deleteDriver(@RequestParam("deleteId") String deleteId){
        driverService.deleteDriver(deleteId);
        return null;
    }

}
