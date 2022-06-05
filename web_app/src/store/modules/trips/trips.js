import axios from "axios"

const state = {
    trips: [],
    my_trip: {},
    // project: {}
}

const getters = {
    getTrips: (state) => state.trips,
    getMyTrip: (state) => state.my_trip,
}

const actions = {
    async fetchTrips({ commit }){
        try{
            let response = await axios.get("get-trips")

            let trips = response.data.data
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setTrips", trips)

            return{
                status: "success",
                message: "Trips successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch trips"
            }
        }
    },

    async createTrip({ commit }, trip){
        let conductor_id = trip["conductor_id"]
        let fleet_id = trip["fleet_id"]
        // let trip_origin = trip["trip_origin"]
        // let trip_destination = trip["trip_destination"]
        let head_count = trip["head_count"]
        let surplus_count = trip["surplus_count"]
        let route_allocation_id = trip["route_allocation_id"]
        let live_route = trip["live_route"]

        try{
            let response = await axios.post("create-trip", {
                conductor_id,
                fleet_id,
                // trip_origin,
                // trip_destination,
                head_count,
                surplus_count,
                route_allocation_id,
                live_route,
            })
            
            trip = response.data.data
            trip = trip[0]
            // console.log(trip)

            commit("addTrip", trip)

            return{
                status: "success",
                message: "Trip successfully created"
            }

        }

        catch(error){
            console.log(error)
            return{
                status: "error",
                message: "We are facing technical challenges"
            }
        }
    },

    async fetchMyTrip({ commit }, conductor_id){
        try{
            let response = await axios.get(`get-my-trip/${conductor_id}`)

            let my_trip = response.data.data
            my_trip = my_trip[0]
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setMyTrip", my_trip)

            return{
                status: "success",
                message: "My trip successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch my trip"
            }
        }
    },

    async offloadTrip({ commit }, my_trip){
        let trip_id = my_trip["_id"]["$oid"]
        let fleet_id = my_trip["fleet"]["_id"]["$oid"]

        try{
            let response = await axios.put("offload-trip", {
                trip_id,
                fleet_id,
            })

            let offloaded_trip = response.data.data
            // offloaded_trip = offloaded_trip[0]
            offloaded_trip = {}
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setMyTrip", offloaded_trip)

            return{
                status: "success",
                message: "My trip successfully offloaded"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to offload my trip"
            }
        }
    },

    async refreshTrip({ commit }, my_trip){
        let trip_id = my_trip["_id"]["$oid"]
        let live_route_track = my_trip["live_route_track"]
        let live_route = my_trip["live_route"]
        let last_pickup_fleet = my_trip["fleet"]["_id"]["$oid"]

        try{
            let response = await axios.put("refresh-trip", {
                trip_id,
                live_route_track,
                live_route,
                last_pickup_fleet
            })

            let refreshed_trip = response.data.data
            refreshed_trip = refreshed_trip[0]
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setMyTrip", refreshed_trip)

            return{
                status: "success",
                message: "My trip successfully refreshed"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to refresh my trip"
            }
        }
    },

    // async allocateFleet({ commit }, fleet){
    //     let conductor_id = fleet["conductor_id"]
    //     let fleet_id = fleet["fleet_id"]

    //     try{
    //         let response = await axios.put("allocate-fleet", {
    //             conductor_id,
    //             fleet_id,
    //         })
            
    //         let allocated_fleet = response.data.data

    //         commit("allocateFleet", allocated_fleet)

    //         return{
    //             status: "success",
    //             message: "Fleet successfully allocated"
    //         }

    //     }

    //     catch(error){
    //         console.log(error)
    //         return{
    //             status: "error",
    //             message: "We are facing technical challenges"
    //         }
    //     }
    // },
}

const mutations = {
    setTrips: (state, trips) => (state.trips = trips),
    addTrip: (state, trip) => (state.trips.unshift(trip)),
    setMyTrip: (state, my_trip) => (state.my_trip = my_trip),
    
    // allocateFleet: (state, allocated_fleet) => {
    //     const index = state.fleets.findIndex(x => x._id.$oid === allocated_fleet["_id"]["$oid"])

    //     if(index !== -1){
    //         state.fleets.splice(index, 1, allocated_fleet)
    //     }
    // },
}

export default{
    state,
    getters,
    actions,
    mutations
}