package com.vehicle.identifier.vicore.controllers;

import java.time.ZonedDateTime;
import java.util.UUID;

import com.vehicle.identifier.vicore.models.User;
import com.vehicle.identifier.vicore.models.Vehicle;
import com.vehicle.identifier.vicore.services.VehicleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;

@Controller
public class VehicleController {
	
	@Autowired
	private VehicleService vehicleService;

	@GetMapping("/vehicles")
	public String getVehicles(Model model) {
		model.addAttribute("addVehicle", new Vehicle());
		model.addAttribute("vehicles", vehicleService.getVehicles());
		return "Vehicle";
	}	
	
	@PostMapping(value ="/vehicles/addNew")
	public String addNew(@ModelAttribute("vehicle") Vehicle vehicle) {
		vehicle.setCreated(ZonedDateTime.now());
		vehicle.setId(String.valueOf(UUID.randomUUID()));
		vehicleService.save(vehicle);
		return "redirect:/vehicles";
	}
	
	@GetMapping("vehicles/findById/{id}")
	public Vehicle findById(@PathVariable("id") String id) {
		System.out.println("here");
	  return vehicleService.findById(id);	
	}	
	
	@RequestMapping(value="/vehicles/update", method= {RequestMethod.PUT, RequestMethod.GET})
	public String update(Vehicle vehicle) {
		vehicleService.save(vehicle);
		return "redirect:/vehicles";
	}
	
	@RequestMapping(value="/vehicles/delete", method= {RequestMethod.DELETE, RequestMethod.GET})
	public String delete(Integer id) {
		vehicleService.delete(id);
		return "redirect:/vehicles";
	}

	@RequestMapping("vehicles/findByLicensePlate")
	@ResponseBody
	public Vehicle findByLicensePlate(String IicensePlate) {
		return vehicleService.getVehicleByLicensePlate(IicensePlate);
	}


	@RequestMapping("vehicles/blacklist")
	@ResponseBody
	public RedirectView blacklistById(String id , RedirectAttributes redir)
	{

		Vehicle vehicle = vehicleService.findById(id);
		vehicle.setBlacklisted(true);
		vehicleService.blacklist(vehicle);
		RedirectView  redirectView= new RedirectView("/vehicles",true);

		redir.addFlashAttribute("message",	"You successfully registered! You can now login");

		return redirectView;}


}
