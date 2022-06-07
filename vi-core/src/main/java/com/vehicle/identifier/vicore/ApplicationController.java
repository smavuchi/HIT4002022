package com.vehicle.identifier.vicore;

import com.vehicle.identifier.vicore.models.Timelog;
import com.vehicle.identifier.vicore.services.TimelogService;
import com.vehicle.identifier.vicore.services.VehicleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class ApplicationController {

	@Autowired
	TimelogService timelogService;

	@Autowired
	VehicleService vehicleService;
	
	@GetMapping("/index")
	public String goHome(Model model) {
		List<Timelog> timelogList = timelogService.getLoggedInTimelogs();
		List<Timelog> timelogs = timelogService.getTodaysTimelogs();
		model.addAttribute("timelogList", timelogList);
		model.addAttribute("totalLogged", timelogList.size());
		model.addAttribute("totalCarsToday", timelogs.size());
		return "index";
	}
	
	@GetMapping("/login")
	public String login() {
		return "login";
	}
	
	@GetMapping("/logout")
	public String logout() {
		return "login";
	}	
	
	@GetMapping("/register")
	public String register() {
		return "register";
	}

	@GetMapping("/accessDenied")
	public String fail(){
		return "accessDenied";
	}

}
