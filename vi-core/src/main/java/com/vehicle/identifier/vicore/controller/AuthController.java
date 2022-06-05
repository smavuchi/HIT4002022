package com.vehicle.identifier.vicore.controller;

import com.vehicle.identifier.vicore.model.User;
import com.vehicle.identifier.vicore.service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    AuthService authService;

    @RequestMapping(method = RequestMethod.GET, value = "/login")
    public ModelAndView login(){
        ModelAndView modelAndView = new ModelAndView("auth/login");
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.POST, value = "/signin")
    public ModelAndView signIn(@RequestParam("password") String password,
                               @RequestParam("username") String username,
                               RedirectAttributes redirectAttributes){

        ModelAndView modelAndView = new ModelAndView("redirect:/auth/login");
        User user =  authService.login(username, password);
        System.out.println(user.getUsername());
        if(user == null){
            System.out.println("im here qwe");
            redirectAttributes.addFlashAttribute("user", user);
            redirectAttributes.addFlashAttribute("displayMessage",
                    "Wrong password");
            return modelAndView;
        }
        if (user.getRole() == "ADMIN"){
            modelAndView.setViewName("redirect:/admin/home/"+ user.getId());
            return modelAndView;
        }
        modelAndView.setViewName("redirect:/user/home/"+ user.getId());
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/home/{userId}")
    public ModelAndView home(@PathVariable("userId") String userId){
        ModelAndView modelAndView = new ModelAndView("home");
        return modelAndView;
    }

    @RequestMapping(method = RequestMethod.GET, value = "/signup")
    public ModelAndView signup(){

        ModelAndView modelAndView = new ModelAndView("/auth/register");
        User user = new User();
        modelAndView.addObject(user);
        return modelAndView;
    }
}
