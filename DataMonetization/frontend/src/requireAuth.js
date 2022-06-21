import {frontend} from "baseUrl";

export default function requireAuth() {
  if ((!localStorage.getItem("api-key")) && (!localStorage.getItem("token"))) {
    window.location = `${frontend}/auth/signin`;
  }
}