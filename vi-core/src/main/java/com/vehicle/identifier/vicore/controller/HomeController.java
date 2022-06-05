package com.vehicle.identifier.vicore.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HomeController {

    @RequestMapping(method = RequestMethod.GET, value = "/welcome")
    public ModelAndView welcome(){
        ModelAndView modelAndView = new ModelAndView("welcome");
        return modelAndView;
    }

    @GetMapping("/index")
    public String goHome() {
        return "/user/index";
    }
}
