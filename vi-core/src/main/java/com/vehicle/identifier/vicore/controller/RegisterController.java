package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.service.RegisterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

@RestController
@RequestMapping("/register")
public class RegisterController {

    @Autowired
    RegisterService registerService;

    @RequestMapping(method = RequestMethod.POST, value = "/user")
    public ModelAndView registerUser(@ModelAttribute("user")User user){
        User user1 = registerService.registerUser(user);
        ModelAndView modelAndView = new ModelAndView("/home");
        modelAndView.addObject(user1);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/driver")
    public ModelAndView registerDriver(@ModelAttribute("driver") Driver driver){
        Driver driver1 = registerService.registerDriver(driver);
        ModelAndView modelAndView = new ModelAndView("redirect:/driver/{driver1}");
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/vehicle")
    public ModelAndView registerVehicle(@ModelAttribute("vehicle")Vehicle vehicle){
        Vehicle vehicle1 = registerService.registerVehicle(vehicle);
        ModelAndView modelAndView = new ModelAndView("redirect:/vehicle/{vehicle1}");
        return modelAndView;
    }
}