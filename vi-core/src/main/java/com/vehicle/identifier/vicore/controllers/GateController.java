package com.vehicle.identifier.vicore.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
@RequestMapping("/gate")
public class GateController {

    @RequestMapping(method = RequestMethod.POST, value = "/open")
    public ModelAndView openGate(){
        return null;
    }
}
