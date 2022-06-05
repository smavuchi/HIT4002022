import axios from "axios"

const state = {
    stations: [],
    stations_status: [],
    station_status_details: {},
    // project: {}
}

const getters = {
    getStations: (state) => state.stations,
    getStationsStatus: (state) => state.stations_status,
    getStationStatusDetails: (state) => state.station_status_details,
}

const actions = {
    async fetchStations({ commit }){
        try{
            let response = await axios.get("get-stations")

            let stations = response.data.data
            
            console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setStations", stations)

            return{
                status: "success",
                message: "Stations successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch stations"
            }
        }
    },

    async fetchStationsStatus({ commit }, prediction_body){
        console.log(prediction_body)
        let prediction_day = prediction_body["prediction_day"]
        let prediction_time = prediction_body["prediction_time"]

        try{
            let response = await axios.post("get-stations-status", {
                prediction_day,
                prediction_time,
            })

            let stations_status = response.data.data
            
            console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setStationsStatus", stations_status)

            return{
                status: "success",
                message: "Stations status successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch stations status"
            }
        }
    },

    async refreshStation({ commit }, refreshed_station){
        console.log(refreshed_station)
        commit("setRefreshedStation", refreshed_station)
    },

    async refreshStationStatusDetails({ commit }, station_status_details){
        // console.log(station_status)
        commit("setStationStatusDetails", station_status_details)
    },

    // async createDepartment({ commit }, department_name){

    //     try{
    //         const response = await axios.post("create_department", {
    //             department_name,
    //         })
            
    //         let status = response.data.status
    //         let department = response.data.data
    //         let message = response.data.message
    //         console.log(department)

    //         commit("addDepartment")

    //         return{
    //             status,
    //             message
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
    setStations: (state, stations) => (state.stations = stations),
    
    setStationsStatus: (state, stations_status) => (state.stations_status = stations_status),

    setStationStatusDetails: (state, station_status_details) => (state.station_status_details = station_status_details),
    
    setRefreshedStation: (state, refreshed_station) => {
        const index = state.stations.findIndex(x => x._id.$oid === refreshed_station["_id"]["$oid"])

        if(index !== -1){
            state.stations.splice(index, 1, refreshed_station)
        }
    },
}

export default{
    state,
    getters,
    actions,
    mutations
}