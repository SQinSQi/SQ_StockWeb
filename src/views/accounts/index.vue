<template>
  <div class="myaccount">
    <panel-group id="panel_group"/>
    <el-table v-loading="loading" :data="tableData">
      <el-table-column label="名称" align="center" prop="name" />
      <el-table-column label="持仓" align="center" prop="position" />
      <el-table-column label="市值" align="center">
        <template slot-scope="scope">
          {{ calculateMarketValue(scope.row.price,scope.row.position) }}
        </template>
      </el-table-column>
      <el-table-column label="现价" align="center" prop="price" />
      <el-table-column label="成本" align="center" prop="buy_price" />
      <el-table-column label="累计盈亏" align="center" prop="profit">
        <template slot-scope="scope">
          {{ calculateProfitValue(scope.row.price,scope.row.buy_price,scope.row.position) }}
        </template>
      </el-table-column>
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
        this.tableData = response.stocks
      })
    },
    calculateMarketValue(a, b) {
      return a*b
    },
    calculateProfitValue(x, y, z){
      return (x-y)*z
    }
  }
}
</script>

<style lang="scss" scoped>
.myaccount {
  padding: 32px;
}
</style>
