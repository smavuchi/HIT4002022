import axios from "axios"

const state = {
    users: [],
    // project: {}
}

const getters = {
    getUsers: (state) => state.users,
}

const actions = {
    async fetchUsers({ commit }){
        try{
            let response = await axios.get("get-users")

            let users = response.data.data
            
            // console.log(response.data)
            // console.log(response.data.message)
            // console.log(response.data.status)
            commit("setUsers", users)

            return{
                status: "success",
                message: "Users successfully fetched"
            }
        }

        catch(error){
            console.log(error)

            return{
                status: "error",
                message: "Failed to fetch users"
            }
        }
    },

    async createUser({ commit }, user){
        let first_name = user["first_name"]
        let last_name = user["last_name"]
        let email = user["email"]
        let password = user["password"]
        let role = user["role"]
        // let allocation_status = fleet["allocation_status"]
        // let fleet_status = fleet["allocation_status"]

        try{
            let response = await axios.post("create-user", {
                first_name,
                last_name,
                email,
                password,
                role,
            })
            
            user = response.data.data
            // console.log(fleet)

            commit("addUser", user)

            return{
                status: "success",
                message: "User successfully created"
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
    setUsers: (state, users) => (state.users = users),

    addUser: (state, user) => (state.users.unshift(user)),

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