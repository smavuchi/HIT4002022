import axios from "axios"

const state = {
    possible_routes: [],
    // project: {}
}

const getters = {
    getPossibleRoutes: (state) => state.possible_routes,
}

const actions = {
    async generateRoutesPredictions({ commit }, route){
        let fleet_capacity = route["fleet_capacity"]
        let current_station = route["current_station"]

        try{
            let response = await axios.post("generate-routes-predictions", {
                fleet_capacity,
                current_station
            })

            let possible_routes = response.data.data
            
            console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setPossibleRoutes", possible_routes)

            return{
                status: "success",
                message: "Done"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed"
            }
        }
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
    setPossibleRoutes: (state, possible_routes) => (state.possible_routes = possible_routes),
    
    // setUpdatedDepartment: (state, department) => {
    //     const index = state.departments.findIndex(x => x.id === department["id"])

    //     if(index !== -1){
    //         state.departments.splice(index, 1, department)
    //     }
    // },
}

export default{
    state,
    getters,
    actions,
    mutations
}