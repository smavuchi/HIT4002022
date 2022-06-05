<template>
  <div>

    <a-modal
      title="Create Route Form"
      :visible="createRouteVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <!-- SHOULD BE SYSTEM GENERATED -->
                <a-col :span="24">
                    <a-form-item class="a-form-item" label="Route" :style="{ marginRight: '6px' }">
                        <a-select
                            v-model="route"
                            mode="multiple"
                            placeholder="Route"
                        >
                            <a-select-option v-for="station in getStations" :key="station['_id']['$oid']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row>

            <a-row>
                <a-col :span="12">
                    <a-form-item>
                        <a-button type="danger" @click.prevent="$emit('handleHide')">cancel</a-button>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item :style="{ float: 'right' }">
                        <a-button type="primary" @click.prevent="saveRoute" :loading="createBtnLoading">save</a-button>
                    </a-form-item>
                </a-col>
            </a-row>
        </a-form>
      </div>
    </a-modal>
  </div>
</template>
<script>
    import { mapActions, mapGetters } from "vuex"
    
    export default {
        name: "CreateRoute",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // Trip Details
                route: [],
                user_id: "",
                fleet_id: "",
                trip_origin: "",
                trip_destination: "",
                head_count: 0,
                surplus_count: 0
            };
        },

        props: {
            createRouteVisible: Boolean,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["createRoute"]),

            // showModal() {
            //     this.visible = true;
            // },

            //   Create Trip
            async saveRoute(){
                this.createBtnLoading = true

                await this.createRoute(this.route).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                    }
                    
                    else if(response.status === "warn"){
                        this.$message.warn(response.message);
                    }
                    
                    else if(response.status === "error"){
                        this.$message.error(response.message);
                    }
                })

                this.createBtnLoading = false
                
                this.$emit('handleHide')
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getStations"]),
    };
</script>