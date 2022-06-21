import axios from "axios";

// Add a request interceptor
axios.interceptors.request.use(function (config) {
  const apiKey = localStorage.getItem("api-key");

  if (apiKey) {
    config.url += (config.url.includes("?") ? "&" : "?") + `api-key=${apiKey}`;
  }
    // Do something before request is sent
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });

axios.interceptors.response.use(response => {
  if (response.data.status == 422)
  {
    localStorage.removeItem("api-key");
    return;
  }
  return response;
}, error => {
  return Promise.reject(error);
});