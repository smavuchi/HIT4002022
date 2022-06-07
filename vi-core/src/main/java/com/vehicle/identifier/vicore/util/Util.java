package com.vehicle.identifier.vicore.util;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.time.ZonedDateTime;
import java.util.UUID;

public class Util {

    public static final  String       DATE_TIME_FORMAT = "yyyy-MM-dd'T'HH:mm:ss.SSSZ";
    private static ObjectMapper objectMapper;
    public static String uuid(){
        UUID uuid = UUID.randomUUID();
        return String.valueOf(uuid);
    }

    public static ZonedDateTime currentTime(){
        return ZonedDateTime.now();
    }
}
