<template>
    <div :style="{ minHeight: '100vh', display: 'flex' }">
        <div :style="{ margin: 'auto', border: '', padding: '24px' }">
            <a-card class="login-card" :style="{ borderRadius: '4px', width: '50%', margin: 'auto' }">
                <a-row :style="{ display: 'flex', border: '',  margin: 'auto', minHeight: '100%' }">
                    <a-col :span="12" :style="{ display: '', width: '', minHeight: '100%', margin: '', border: '', borderRadius: '4px' }">
                        <img src="images/commuting.jpg" :style="{ margin: '', width: '100%', height: '100%', borderRadius: '4px' }">
                    </a-col>

                    <a-col :span="12" :style="{ display: '', minHeight: '100%', margin: 'auto', border: '' }">
                        <h3 :style="{ textAlign: '', fontSize: '24px', fontWeight: 'bold', margin: '12px' }">Passengers Prediction</h3>
                
                        <a-form
                            id="components-form-demo-normal-login"
                            :form="form"
                            class="login-form"
                            @submit="handleSubmit"
                            :style="{ padding: '12px', margin: '' }"
                        >
                            <a-form-item>
                                    <a-input
                                        v-model="email"
                                        placeholder="Email"
                                    >
                                        <a-icon slot="prefix" type="mail" style="color: rgba(0,0,0,.25)" />
                                    </a-input>
                            </a-form-item>

                            <a-form-item>
                                    <a-input-password
                                        v-model="password"
                                        type="password"
                                        placeholder="Password"
                                    >
                                        <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
                                    </a-input-password>
                            </a-form-item>

                            <a-form-item>
                                <a-button type="primary" html-type="submit" class="login-form-button" :loading="loginBtnLoading" @click.prevent="authenticate" :disabled="invalid">
                                    Log in
                                </a-button>
                                
                            </a-form-item>

                            <!-- <a-form-item :style="{ textAlign: 'center' }">
                                <a-button type="default" :style="{ width: '50%', margin: 'auto' }">
                                    Register
                                </a-button>
                            </a-form-item> -->
                        </a-form>
                    </a-col>
                </a-row>
            </a-card>
        </div>
    </div>
</template>

<script>
    import { mapActions, mapGetters } from "vuex"

    export default {
        name: "Login",

        components: {},
        
        data(){
            return{
                registerBtnLoading: false,
                loginBtnLoading: false,
                email: "",
                password: "",
            }
        },
        
        methods: {
            // ...mapActions(["login", "activate"]),
            ...mapActions(["login"]),

            handleSubmit() {
                console.log("Handle submit")
            },

            async authenticate(){
                // console.log("Authenticate")
                // this.$router.push({ name: "Dashboard" })
                this.loginBtnLoading = true

                let user = {
                    email: this.email,
                    password: this.password
                }

                await this.login(user).then((response) => {
                    if(response["status"] === "success"){
                        this.$message.success(response["message"])

                        if(this.getActiveUser["role"] === "DISPATCHER"){
                            this.$router.push({ name: "Stations Status" })
                        }

                        else if(this.getActiveUser["role"] === "CONDUCTOR"){
                            this.$router.push({ name: "Route Allocations" })
                        }
                    }

                    else if(response["status"] === "error"){
                        this.$message.error(response["message"])
                    }
                })

                this.loginBtnLoading = false
            },

            // async register(){
            //     this.registerBtnLoading = true

            //     await this.$router.push({ name: "Register" })

            //     this.registerBtnLoading = false
            // },

            // async authenticate(){
            //     this.loginBtnLoading = true

            //     let user = {
            //         email: this.email,
            //         password: this.password,
            //     }

            //     await this.login(user).then((response) => {
            //         if(response.status === "info"){
            //             this.$message.info(response.message);
            //         }
                    
            //         else if(response.status === "success"){
            //             let user_id = response.user.first_name.toLowerCase()
                        
            //             CometChat.login(user_id, COMETCHAT_CONSTANTS.AUTH_KEY).then((user) => {
            //                 this.$message.success(response.message);
            //                 this.activate(true)
            //                 this.$router.replace({ name: "Dashboard" })
            //                 console.log("User logged in : ", user)
            //             })
            //             .catch((error) => {
            //                 this.$message.error("Sorry we could not authenticate chat credentials, please contact technical team")
            //                 console.log('Error in [login]', error)
            //             })
            //         }
                    
            //         else if(response.status === "warn"){
            //             this.$message.warn(response.message);
            //         }
                    
            //         else if(response.status === "error"){
            //             this.$message.error(response.message);
            //         }
            //     })

            //     this.loginBtnLoading = false
            // }
        },

        created(){
            // console.log(this.getLoggedIn)
            // if(this.getLoggedIn){
            //     console.log(this.getLoggedIn)
            //     this.$router.replace({ name: "Dashboard" })
            // }
        },

        computed: mapGetters(["getActiveUser"])
    }
</script>
<style>
    #components-form-demo-normal-login .login-form {
    max-width: 300px;
    }
    #components-form-demo-normal-login .login-form-forgot {
    float: right;
    }
    #components-form-demo-normal-login .login-form-button {
    width: 100%;
    }

    .login-card{
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
</style>
