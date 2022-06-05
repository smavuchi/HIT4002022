import axios from "axios"
import jwt_decode from "jwt-decode"

const state = {
  token: "",
  active_user: {},
  logged_in: false,
};

const getters = {
    getActiveUser: (state) => state.active_user,
    getIsLoggedIn: (state) => state.logged_in,
}

const actions = {
    async login({ commit }, user){

        try{

            const response = await axios.post("login", user)
            
            let status = response["data"]["status"]

            if(status === "200"){
                let access_token = response["data"]["token"]
                let user_data = jwt_decode(access_token)
                let active_user = user_data["sub"]
                
                commit("setActiveUser", active_user)

                return{
                    status: "success",
                    message: "Successfully logged in"
                }
            }

            else{
                // console.log("Incorrect credentials")
                
                return{
                    status: "error",
                    message: "Incorrect credentials"
                }
            }

            // else{
            //     console.log("Server technical problem")

            //     return{
            //         status: "error",
            //         message: response["data"]["message"]
            //     }
            // }
        }

        catch(error){
            console.log(error.response)

            if(error.response.status === 401){
                return{
                    status: "error",
                    message: "Invalid username or password"
                }
            }

            else{
                return{
                    status: "error",
                    message: "Server technical problem"
                }
            }
        }
    },

    async attempt({ commit }, access_token){
        let user_data = jwt_decode(access_token)
        let active_user = user_data["user"]
        let is_verified = user_data["isVerified"]
        
        if(is_verified){
            console.log(active_user)
            commit("setToken", access_token)
            commit("setActiveUser", active_user)
            commit("setIsLoggedIn", true)

            return{
                status: "success",
                message: "Successfully logged in"
            }
        }

        else{
            return{
                status: "error",
                message: "You are not verified"
            }
        }
    },

    async logoutUser({ commit }, bool){
        commit("setIsLoggedIn", bool)
    }
}

const mutations = {
    setToken: (state, access_token) => state.access_token = access_token,
    setActiveUser: (state, active_user) => state.active_user = active_user,
    setIsLoggedIn: (state, logged_in) => state.logged_in = logged_in,
}

export default{
    state,
    getters,
    actions,
    mutations
}