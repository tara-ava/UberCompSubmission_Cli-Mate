<template>
    <div class="overflow-auto">
        <b-card
            title= "Waste" >
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            size="sm"
            aria-controls="my-table" >
        </b-pagination>
        <b-table
            id="my-table"
            :items="items"
            :fields="fields"
            :per-page="perPage"
            :current-page="currentPage"
            striped
            small >
            <template #cell(is_active)="data">
                <b-badge v-if="data.item.is_active" variant="success">
                    Enabled</b-badge>
                <b-badge v-else variant="danger">Disabled</b-badge>
            </template>
            <template #cell(action)="data">
                <b-button-group size="sm">
                <b-button :to="getEditLink(data.item.id)" variant="success">
                    Edit</b-button>
                <b-button @click="delStaff(data.item.id)" variant="warning">
                    Delete</b-button>
                </b-button-group>
            </template>
        </b-table>
        </b-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
            perPage: 5,
            currentPage: 1,
            items: [], // cards
            tmp1: [],
        fields: [
          'wtype',
          'weight',
          'date',
          'available',          
         ],
      }
    },
    methods: {
        getShowLink (id) {
            return ('/cards/show/' + id.toString())
        },
        getEditLink (id) {
            console.log('/cards/edit/' + id)
            return ('/cards/edit/' + id.toString())
        },
        async delete(id) {
            console.log('delete: ' +id)
            const r = await this.$axios.$delete(
                'http://127.0.0.1:3333/cards/' + id)
            .then(res => {
                this.$fetch()
            })
            .catch(err => {
                console.log(err)
            })
            return r
        },
        delStaff (id) {
            this.$bvModal.msgBoxConfirm('Are you sure?')
            .then(value => {
                if (value == true) {
                    console.log('delStaff: confirm delete')
                    this.delete(id)
                }
                else {
                    console.log('delStaff: cancel delete')
                }
            })
            .catch(err => {
                console.log('delStaff: something is wrong')
            })
        },
    },
    computed: {
        rows() {
            return this.items.length
        }
    },
    async fetch() {
      this.tmp1 = await fetch(
        'http://127.0.0.1:8888/waste'
      ).then(res => res.json())
      this.items = this.tmp1.data
   }
}
</script>

