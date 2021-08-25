<template>
  <div class="myaccount">
    <panel-group id="panel_group"/>
    <el-table class="stocksTable" v-loading="loading" :data="tableData" stripe>
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
      <el-table-column
        label="操作"
        align="center"
        width="160"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            icon="el-icon-sort"
            @click="handleUpdate(scope.row)"
            >买入/卖出</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-row class="editAccount">
      <el-button type="info" size="primary" @click=addStock()>新增持仓</el-button>
    </el-row>

    <el-dialog :title="title" :visible.sync="open" width="40%" center>
      <el-form
        :model="form"
        label-width=" 150px"
        :rules="dialogFormRules"
        ref="form"
      >
      <el-row>
        <el-col :span="12">
          <el-form-item label="买入：" prop="addposition">
            <el-input v-model="form.addposition" placeholder="请输入买入股数" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="价格：" prop="addprice">
            <el-input v-model="form.addprice" placeholder="请输入买入股价" />
          </el-form-item>
        </el-col>
      </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取消</el-button>
        <el-button type="primary" @click="submitForm">确定</el-button>
      </span>
    </el-dialog>
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
      // 遮罩层
      loading: false,
      // 获得列表数据
      tableData: [],
      // 弹窗标题
      title: "",
      // 弹窗控制
      open: false,
      // 新增股票
      form:{},
      
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
.editAccount {
  margin-top: 20px;
}
.stocksTable {
  margin-top: 20px;
}
</style>
