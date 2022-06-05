import axios from "axios"

const state = {
    conductors: [],
    // project: {}
}

const getters = {
    getConductors: (state) => state.conductors,
}

const actions = {
    async fetchConductors({ commit }){
        try{
            let response = await axios.get("get-conductors")

            let conductors = response.data.data
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setConductors", conductors)

            return{
                status: "success",
                message: "Conductors successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch conductors"
            }
        }
    },

    // async createConductor({ commit }, conductor){
    //     let conductor_number = conductor["conductor_number"]
    //     let conductor_capacity = conductor["conductor_capacity"]
    //     let allocation_status = conductor["allocation_status"]
    //     let conductor_status = conductor["allocation_status"]

    //     try{
    //         let response = await axios.post("create-conductor", {
    //             conductor_number,
    //             conductor_capacity,
    //             allocation_status,
    //             conductor_status,
    //         })
            
    //         conductor = response.data.data
    //         // console.log(conductor)

    //         commit("addConductor", conductor)

    //         return{
    //             status: "success",
    //             message: "Conductor successfully created"
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
    setConductors: (state, conductors) => (state.conductors = conductors),

    // addConductor: (state, conductor) => (state.conductors.unshift(conductor)),
    
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