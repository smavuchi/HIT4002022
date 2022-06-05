<template>
  <div>

    <a-modal
      :title="'Allocate Fleet '+ fleet['fleet_number']"
      :visible="allocateFleetVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <a-col :span="24">
                    <a-form-item class="a-form-item" label="Conductor" :style="{ marginRight: '6px' }">
                        <a-select v-model="conductor_id" placeholder="Conductor">
                            <a-select-option v-for="conductor in getConductors" :key="conductor['_id']['$oid']" :value="conductor['_id']['$oid']">{{ conductor["first_name"] }} {{ conductor["last_name"] }}</a-select-option>
                            <!-- <a-select-option value="FREE">John Doe</a-select-option>
                            <a-select-option value="ALLOCATED">Foo Bar</a-select-option> -->
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
                        <a-button type="primary" @click.prevent="toAllocateFleet" :loading="allocateBtnLoading">allocate</a-button>
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
        name: "AllocateFleet",

        data() {
            return {
                allocateBtnLoading: false,
                disabled: true,

                // Route Details
                conductor_id: "",
                // company: this.getActiveUser["company"],
            };
        },

        props: {
            allocateFleetVisible: Boolean,
            fleet: Object,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["allocateFleet"]),

            //   Request Route
            async toAllocateFleet(){
                // this.$router.push({ name: "Appropriate Route" })
                this.allocateBtnLoading = true

                let fleet = {
                    conductor_id: this.conductor_id,
                    fleet_id: this.fleet["_id"]["$oid"],
                }

                await this.allocateFleet(fleet).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                        this.$router.push({ name: "Fleets" })
                    }
                    
                    else if(response.status === "warn"){
                        this.$message.warn(response.message);
                    }
                    
                    else if(response.status === "error"){
                        this.$message.error(response.message);
                    }
                })

                this.allocateBtnLoading = false
                this.$emit('handleHide')
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getFleets", "getConductors"]),
    };
</script>