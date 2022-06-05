package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.Optional;

@RestController
@RequestMapping("/admin")
public class AdminController {

    @Autowired
    UserService userService;

    @RequestMapping(method = RequestMethod.GET, value = "/home/{userId}")
    public ModelAndView home(@PathVariable("userId") String userId){
        Optional<User> user = userService.findUserById(userId);
        ModelAndView modelAndView = new ModelAndView("/user/home");
        modelAndView.addObject(user);
        return modelAndView;
    }
}
