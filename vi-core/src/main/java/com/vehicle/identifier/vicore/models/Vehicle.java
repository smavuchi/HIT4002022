package com.vehicle.identifier.vicore.models;

import javax.persistence.*;

@Entity
@Table(name = "vehicle")
public class Vehicle extends Base{

	public boolean blacklisted;
	public String color;
	public String licensePlate;
	public String status;
	public String make;
	public String model;
	public String driverId;

	public Vehicle(boolean blacklisted, String color, String licensePlate, String status, String make, String model) {
		super();
	}

	public Vehicle() {

	}

	public Vehicle toParameters(){
		return new Vehicle(blacklisted, color, licensePlate, status, make, model);
	}

	public boolean isBlacklisted() {
		return blacklisted;
	}

	public void setBlacklisted(boolean blacklisted) {
		this.blacklisted = blacklisted;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getLicensePlate() {
		return licensePlate;
	}

	public void setLicensePlate(String licensePlate) {
		this.licensePlate = licensePlate;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getMake() {
		return make;
	}

	public void setMake(String make) {
		this.make = make;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getDriverId() {
		return driverId;
	}

	public void setDriverId(String driverId) {
		this.driverId = driverId;
	}
}
