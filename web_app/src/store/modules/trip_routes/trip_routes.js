import axios from "axios"

const state = {
    // routes: [],
    route_allocations: [],
    route_allocation: {},
    // project: {}
}

const getters = {
    // getRoutes: (state) => state.routes,
    getRouteAllocations: (state) => state.route_allocations,
    getVisualRoute: (state) => state.route_allocation,
    // getMyRoute: (state) => state.my_route,
}

const actions = {
    async fetchRouteAllocations({ commit }, user_id){
        // let user_id = route_allocations["user_id"]

        try{
            let response = await axios.get(`get-route-allocations/${user_id}`)

            let route_allocations = response.data.data
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setRouteAllocations", route_allocations)

            return{
                status: "success",
                message: "Route allocations successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch route allocations"
            }
        }
    },

    async createRoute({ commit }, route){
        try{
            let response = await axios.post("create-possible-route", {
                route,
            })
            
            let new_route = response.data.data
            new_route = new_route[0]
            // console.log(route)

            commit("addRoute", new_route)

            return{
                status: "success",
                message: "Route successfully created"
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

    async allocateRoute({ commit }, route){
        let conductor_id = route["conductor_id"]
        let fleet_id = route["fleet_id"]
        let optimal_route = route["optimal_route"]
        try{
            let response = await axios.post("allocate-route", {
                conductor_id,
                fleet_id,
                optimal_route,
            })
            
            let new_allocated_route = response.data.data
            new_allocated_route = new_allocated_route[0]
            // console.log(route)

            commit("addAllocatedRoute", new_allocated_route)

            return{
                status: "success",
                message: "Route successfully allocated"
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

    // async fetchMyroute({ commit }, user_id){
    //     try{
    //         let response = await axios.get(`get-my-route/${user_id}`)

    //         let my_route = response.data.data
    //         my_route = my_route[0]
            
    //         // console.log(response.data)
    //         // console.log(response.data.message)
    //         // console.log(response.data.status)
    //         commit("setMyroute", my_route)

    //         return{
    //             status: "success",
    //             message: "My route successfully fetched"
    //         }
    //     }

    //     catch(error){
    //         console.log(error)

    //         return{
    //             status: "error",
    //             message: "Failed to fetch my route"
    //         }
    //     }
    // },

    // async offloadroute({ commit }, my_route){
    //     let route_id = my_route["_id"]["$oid"]

    //     try{
    //         let response = await axios.put("offload-route", {
    //             route_id,
    //         })

    //         let offloaded_route = response.data.data
    //         // offloaded_route = offloaded_route[0]
    //         offloaded_route = {}
            
    //         // console.log(response.data)
    //         // console.log(response.data.message)
    //         // console.log(response.data.status)
    //         commit("setMyroute", offloaded_route)

    //         return{
    //             status: "success",
    //             message: "My route successfully offloaded"
    //         }
    //     }

    //     catch(error){
    //         console.log(error)

    //         return{
    //             status: "error",
    //             message: "Failed to offload my route"
    //         }
    //     }
    // },

    async refreshVisualRoute({ commit }, route_allocation){
        
        commit("setVisualRoute", route_allocation)
    },

    async refreshNewRouteAllocation({ commit }, new_route_allocation){
        console.log(new_route_allocation)
        commit("setRefreshedNewRouteAllocation", new_route_allocation)
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
    setRouteAllocations: (state, route_allocations) => (state.route_allocations = route_allocations),
    // addRoute: (state, new_route) => (state.routes.unshift(new_route)),
    addAllocatedRoute: (state, new_allocated_route) => (state.route_allocations.push(new_allocated_route)),
    setVisualRoute: (state, route_allocation) => (state.route_allocation = route_allocation),
    
    // allocateFleet: (state, allocated_fleet) => {
    //     const index = state.fleets.findIndex(x => x._id.$oid === allocated_fleet["_id"]["$oid"])

    //     if(index !== -1){
    //         state.fleets.splice(index, 1, allocated_fleet)
    //     }
    // },

    setRefreshedNewRouteAllocation: (state, new_route_allocation) => (state.route_allocations.unshift(new_route_allocation)),
}

export default{
    state,
    getters,
    actions,
    mutations
}