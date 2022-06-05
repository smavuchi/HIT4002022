package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    UserService userService;

    @RequestMapping(method = RequestMethod.GET, value = "/home/{userId}")
    public ModelAndView home(@PathVariable("userId") String userId){
        Optional<User> user = userService.findUserById(userId);
        ModelAndView modelAndView = new ModelAndView("/user/home");
        modelAndView.addObject(user);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/{userId}")
    public ModelAndView getUser(@RequestParam("userId") String userId){
        Optional<User> user = userService.findUserById(userId);
        ModelAndView modelAndView = new ModelAndView("/user/view");
        modelAndView.addObject(user);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/delete/{userId}")
    public ModelAndView deleteUser(@RequestParam("userId") String userId){
        userService.deleteUser(userId);
        return null;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/all")
    public ModelAndView getUsers(@RequestBody User user){
        List<User> users = userService.findAllUsers();
        ModelAndView modelAndView = new ModelAndView("/user/list");
        modelAndView.addObject(users);
        return modelAndView;
    }

    @GetMapping("/index")
    public String goHome() {
        return "/user/index";
    }
}
