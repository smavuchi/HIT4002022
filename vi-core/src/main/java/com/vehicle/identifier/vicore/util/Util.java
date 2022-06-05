package com.vehicle.identifier.vicore.util;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

import java.text.SimpleDateFormat;
import java.time.ZonedDateTime;
import java.util.UUID;

public class Util {

    public static final  String       DATE_TIME_FORMAT = "yyyy-MM-dd'T'HH:mm:ss.SSSZ";
    private static       ObjectMapper objectMapper;

    static {
        objectMapper = new ObjectMapper();
        objectMapper.configure(SerializationFeature.INDENT_OUTPUT, true);
        objectMapper.registerModule(new JavaTimeModule());
        objectMapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, true);
        objectMapper.setDateFormat(new SimpleDateFormat(DATE_TIME_FORMAT));
        objectMapper.disable(DeserializationFeature.ADJUST_DATES_TO_CONTEXT_TIME_ZONE);
    }

    public static String uuid(){
        UUID uuid = UUID.randomUUID();
        return String.valueOf(uuid);
    }

    public static ZonedDateTime currentTime(){
        return ZonedDateTime.now();
    }

    public static String toJson(Object object) throws JsonProcessingException {
        objectMapper.configure(SerializationFeature.WRAP_EXCEPTIONS, false);
        return objectMapper.writeValueAsString(object);
    }

    public static <T> T fromJson(String string, Class<T> type) throws JsonProcessingException {
        return objectMapper.readValue(string, type);
    }
}
