import axios from "axios"

const state = {
    fleets: [],
    // project: {}
}

const getters = {
    getFleets: (state) => state.fleets,
    getFreeFleets: (state) => state.fleets.filter(fleet => fleet.fleet_status === "FREE" && fleet.allocation_status === "ALLOCATED"),
    getOccupiedFleets: (state) => state.fleets.filter(fleet => fleet.fleet_status === "OCCUPIED" && fleet.allocation_status === "ALLOCATED"),
}

const actions = {
    async fetchFleets({ commit }){
        try{
            let response = await axios.get("get-fleets")

            let fleets = response.data.data
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setFleets", fleets)

            return{
                status: "success",
                message: "Fleets successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch fleets"
            }
        }
    },

    async createFleet({ commit }, fleet){
        let fleet_number = fleet["fleet_number"]
        let fleet_capacity = fleet["fleet_capacity"]
        let current_station = fleet["current_station"]
        // let allocation_status = fleet["allocation_status"]
        // let fleet_status = fleet["allocation_status"]

        try{
            let response = await axios.post("create-fleet", {
                fleet_number,
                fleet_capacity,
                current_station,
                // allocation_status,
                // fleet_status,
            })
            
            fleet = response.data.data
            fleet = fleet[0]
            // console.log(fleet)

            commit("addFleet", fleet)

            return{
                status: "success",
                message: "Fleet successfully created"
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

    async allocateFleet({ commit }, fleet){
        let conductor_id = fleet["conductor_id"]
        let fleet_id = fleet["fleet_id"]

        try{
            let response = await axios.put("allocate-fleet", {
                conductor_id,
                fleet_id,
            })
            
            let allocated_fleet = response.data.data

            commit("allocateFleet", allocated_fleet)

            return{
                status: "success",
                message: "Fleet successfully allocated"
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

    async refreshFleet({ commit }, refreshed_fleet){
        console.log(refreshed_fleet)
        commit("setRefreshedFleet", refreshed_fleet)
    },
}

const mutations = {
    setFleets: (state, fleets) => (state.fleets = fleets),

    addFleet: (state, fleet) => (state.fleets.unshift(fleet)),
    
    allocateFleet: (state, allocated_fleet) => {
        const index = state.fleets.findIndex(x => x._id.$oid === allocated_fleet["_id"]["$oid"])

        if(index !== -1){
            state.fleets.splice(index, 1, allocated_fleet)
        }
    },

    setRefreshedFleet: (state, refreshed_fleet) => {
        const index = state.fleets.findIndex(x => x._id.$oid === refreshed_fleet["_id"]["$oid"])

        if(index !== -1){
            state.fleets.splice(index, 1, refreshed_fleet)
        }
    },
}

export default{
    state,
    getters,
    actions,
    mutations
}