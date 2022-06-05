import Vue from "vue";
import VueRouter from "vue-router";

// Layouts
import DashboardLayout from "../components/layouts/DashboardLayout.vue"
import BlankLayout from "../components/layouts/BlankLayout.vue"

// Pages
import Login from "../components/auth/Login.vue"
import Dashboard from "../components/dashboard/Dashboard.vue"
import Predictions from "../components/predictions/Predictions.vue"
import AllTrips from "../components/trips/AllTrips.vue"
import MyTrip from "../components/trips/MyTrip.vue"
import Fleets from "../components/fleets/Fleets.vue"
import StationsStatus from "../components/stations/StationsStatus.vue"
import StationStatusDetails from "../components/stations/StationStatusDetails.vue"
import Conductors from "../components/conductors/Conductors.vue"
import Users from "../components/users/Users.vue"
import RouteAllocations from "../components/routes/RouteAllocations.vue"
import AppropriateRoute from "../components/routes/AppropriateRoute.vue"
import VisualRoute from "../components/routes/VisualRoute.vue"

// Vuex Store
// import store from '../store/store';

const routes = [
    {
      path: "/",
      name: "Login",
      component: Login,
      meta: {
        layout: BlankLayout,
      }
    },
  
    {
      path: "/dashboard",
      name: "Dashboard",
      component: Dashboard,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/predictions",
      name: "Predictions",
      component: Predictions,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/all_trips",
      name: "All Trips",
      component: AllTrips,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/my-trip",
      name: "My Trip",
      component: MyTrip,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/fleets",
      name: "Fleets",
      component: Fleets,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/stations-status",
      name: "Stations Status",
      component: StationsStatus,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/station-status-details",
      name: "Station Status Details",
      component: StationStatusDetails,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/conductors",
      name: "Conductors",
      component: Conductors,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/users",
      name: "Users",
      component: Users,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/route-allocations",
      name: "Route Allocations",
      component: RouteAllocations,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/appropriate-route",
      name: "Appropriate Route",
      component: AppropriateRoute,
      meta: {
        layout: DashboardLayout,
      }
    },

    {
      path: "/visual-route",
      name: "Visual Route",
      component: VisualRoute,
      meta: {
        layout: DashboardLayout,
      }
    },
]

Vue.use(VueRouter);

const router = new VueRouter({
  routes,
  mode: "history",
  linkExactActiveClass: "nav-item active"
});

// router.beforeEach((to, from, next) => {
//   let getLoggedIn = store.getters.getIsLoggedIn;

//   if (to.name !== 'Login') {
//     if (getLoggedIn) {
//       next();
//     } else {
//       next({ name: 'Login' });
//       // next(false)
//     }
//   } else {
//     next();
//   }
// });

export default router;