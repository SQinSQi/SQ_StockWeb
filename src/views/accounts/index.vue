<template>
  <div class="myaccount">
    <panel-group id="panel_group"/>
    <el-table v-loading="loading" :data="tableData">
      <el-table-column label="名称" align="center" prop="stockname" />
      <el-table-column label="市值" align="center">
        <template slot-scope="scope">
          {{ scope.row.stockprice*scope.row.position }}
        </template>
      </el-table-column>
      <el-table-column label="现价" align="center" prop="stockprice" />
      <el-table-column label="累计盈亏" align="center" prop="profit" />
    </el-table>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import { getStocks } from '@/api/mystocks'

export default {
  name: 'Accounts',
  components: {
    PanelGroup
  },
  data() {
    return {
      loading: false,
      tableData: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getStocks().then(response => {
        this.tableData = response
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.myaccount {
  padding: 32px;
}
</style>
