import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

// STORE MODULES
// import auth from './modules/auth/auth';
// import dashboard from './modules/dashboard/dashboard';
import auth from './modules/auth/auth';
import stations from './modules/stations/stations';
import fleets from './modules/fleets/fleets';
import conductors from './modules/conductors/conductors';
import users from './modules/users/users';
import trips from './modules/trips/trips';
import trip_routes from './modules/trip_routes/trip_routes';
import possible_routes from './modules/possible_routes/possible_routes';

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.sessionStorage,
});

const store = new Vuex.Store({
  modules: {
    auth,
    stations,
    fleets,
    conductors,
    users,
    trips,
    trip_routes,
    possible_routes,
  },

  plugins: [vuexLocal.plugin],
});

export default store;
