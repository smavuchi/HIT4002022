package com.vehicle.identifier.vicore.controller;

import org.springframework.web.bind.annotation.PathVariable;
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