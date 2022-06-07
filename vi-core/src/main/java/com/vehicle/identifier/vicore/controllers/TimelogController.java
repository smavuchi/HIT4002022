package com.vehicle.identifier.vicore.controllers;

import com.vehicle.identifier.vicore.models.Timelog;
import com.vehicle.identifier.vicore.services.TimelogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class TimelogController {

    @Autowired
    TimelogService timelogService;

    @GetMapping("/timelog")
    public String getTimelogs(Model model) {
        model.addAttribute("timelogList", timelogService.getTodaysTimelogs());
        return "Timelog";
    }

    @GetMapping("timelog/findById/{id}")
    public Timelog findById(@PathVariable("id") String id) {
        System.out.println("here");
        return timelogService.findById(id);
    }
}
