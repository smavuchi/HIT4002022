<template>
    <div>
        <div class="loading-spinner" v-if="loading">
            <!-- <a-spin /> -->
            <a-skeleton active />
        </div>

        <div v-if="!loading">
            <h1 :style="{ margin: '12px 12px 0' }">Dashboard</h1>
            
            <a-layout-content :style="{ margin: '12px 12px 0' }">
                <div :style="{ background: '#fff' }">

                    <div :style="{ background: '#ECECEC', padding: '12px', textAlign: 'center' }">
                        <a-row :gutter="16" :style="{ margin: '12px 0' }">
                            <a-col :span="8">
                                <a-card>
                                    <a-statistic
                                        title="Fleet"
                                        value=9
                                        :value-style="{ color: '#3f8600', fontSize: '30px' }"
                                        style="margin-right: 12px"
                                    >
                                </a-statistic>
                                </a-card>
                            </a-col>

                            <a-col :span="8">
                                <a-card>
                                    <a-statistic
                                        title="Stations"
                                        value=10
                                        :value-style="{ color: '#cf1322', fontSize: '30px' }"
                                        style="margin-right: 12px"
                                    >
                                    </a-statistic>
                                </a-card>
                            </a-col>

                            <a-col :span="8">
                                <a-card>
                                    <a-statistic
                                        title="Route"
                                        value=10
                                        :value-style="{ color: '#cf1322', fontSize: '30px' }"
                                        style="margin-right: 12px"
                                    >
                                    </a-statistic>
                                </a-card>
                            </a-col>
                        </a-row>
                    </div>
                </div>
            </a-layout-content>
        </div>
    </div>
</template>

<script>
    import { mapActions } from "vuex"

    export default{
        name: "Dashboard",

        data(){
            return{
                loading: false,
                createBtnDisabled: true,
            }
        },

        methods: {
            ...mapActions(["fetchStations", "fetchConductors", "fetchFleets"]),

            // openCreateSchedule(){
            //     this.$router.push({ name: "CreateProject" })
            // }
        },

        async created(){
            this.loading = true
            await this.fetchStations().then((response) => {
                if(response.status === "info"){
                    this.$message.info(response.message);
                }
                
                else if(response.status === "success"){
                    // this.$message.success(response.message);
                }
                
                else if(response.status === "warn"){
                    this.$message.warn(response.message);
                }
                
                if(response.status === "error"){
                    this.$message.error(response.message);
                }
            })

            await this.fetchFleets().then((response) => {
                if(response.status === "info"){
                    this.$message.info(response.message);
                }
                
                else if(response.status === "success"){
                    // this.$message.success(response.message);
                }
                
                else if(response.status === "warn"){
                    this.$message.warn(response.message);
                }
                
                if(response.status === "error"){
                    this.$message.error(response.message);
                }
            })

            await this.fetchConductors().then((response) => {
                if(response.status === "info"){
                    this.$message.info(response.message);
                }
                
                else if(response.status === "success"){
                    // this.$message.success(response.message);
                }
                
                else if(response.status === "warn"){
                    this.$message.warn(response.message);
                }
                
                if(response.status === "error"){
                    this.$message.error(response.message);
                }
            })

            // await this.fetchAllDepartments().then((response) => {
                // if(response.status === "info"){
                //     this.$message.info(response.message);
                // }
                
                // else if(response.status === "success"){
                //     this.$message.success(response.message);
                // }
                
                // else if(response.status === "warn"){
                //     this.$message.warn(response.message);
                // }
                
        //         if(response.status === "error"){
        //             this.$message.error(response.message);
        //         }
        //     })
            this.loading = false
        },

        // mounted(){
        //     if(this.getActiveUser["role"]["role_name"].toLowerCase() === "manager"){
        //         this.createBtnDisabled = false
        //     }

        //     else{
        //         this.createBtnDisabled = true
        //     }
        // },

        // computed: mapGetters(["getDashboard", "getActiveUser"])
    }
</script>