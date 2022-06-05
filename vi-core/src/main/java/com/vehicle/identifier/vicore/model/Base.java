package com.vehicle.identifier.vicore.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.time.ZonedDateTime;

@MappedSuperclass
public class Base {
    @Id
    @GenericGenerator(name = "uuid", strategy = "uuid2")
    private String  id;
    private ZonedDateTime created;
    private ZonedDateTime deleted;
    private ZonedDateTime updated;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ZonedDateTime getCreated() {
        return created;
    }

    public void setCreated(ZonedDateTime created) {
        this.created = created;
    }

    public ZonedDateTime getDeleted() {
        return deleted;
    }

    public void setDeleted(ZonedDateTime deleted) {
        this.deleted = deleted;
    }

    public ZonedDateTime getUpdated() {
        return updated;
    }

    public void setUpdated(ZonedDateTime updated) {
        this.updated = updated;
    }
}
