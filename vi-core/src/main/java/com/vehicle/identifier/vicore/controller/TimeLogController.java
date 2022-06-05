package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;
import com.vehicle.identifier.vicore.service.TimeLogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/timelog")
public class TimeLogController {

    @Autowired
    TimeLogService timeLogService;

    @RequestMapping(method = RequestMethod.POST, value = "/{timelogId}")
    public ModelAndView getTimelog(@PathVariable("timelogId") String timelogId){
        ModelAndView modelAndView = new ModelAndView("timelog/view");
        Optional<TimeLog> timeLog = timeLogService.getTimeLogById(timelogId);
        modelAndView.addObject(timeLog);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/current")
    public ModelAndView getAllTimelogs(){
        ModelAndView modelAndView = new ModelAndView("timelog/list");
        List<TimeLog> timeLogList = timeLogService.getAllCurrentLogs();
        System.out.println(timeLogList.size());
        modelAndView.addObject(timeLogList);
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/delete/{timelogId}")
    public ModelAndView deleteTimelog(){
        return null;
    }
}
