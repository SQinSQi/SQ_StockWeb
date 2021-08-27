<template>
  <div class="myaccount">
    <panel-group id="panel_group"/>
    <el-table class="stocksTable" v-loading="loading" :data="tableData" stripe>
      <el-table-column label="名称" align="center" prop="name" />
      <el-table-column label="持仓" align="center" prop="position" />
      <el-table-column label="市值(人民币)" align="center">
        <template slot-scope="scope">
          {{ fix2(calculateMarketValue(scope.row.price,scope.row.position)) }}
        </template>
      </el-table-column>
      <el-table-column label="现价(人民币)" align="center" prop="price" />
      <el-table-column label="成本(人民币)" align="center" prop="buy_price" />
      <el-table-column label="累计盈亏(人民币)" align="center" prop="profit">
        <template slot-scope="scope">
          {{ fix2(calculateProfitValue(scope.row.price,scope.row.buy_price,scope.row.position)) }}
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        align="center"
        width="300"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="scope">
          <el-row>
            <el-button
              size="mini"
              type="success"
              icon="el-icon-sort-down"
              @click="addStock(scope.row)"
              >买入</el-button>          
            <el-button
              size="mini"
              type="danger"
              icon="el-icon-sort-up"
              @click="sellStock(scope.row)"
              >卖出</el-button>
            <el-button
              size="mini"
              type="warning"
              icon="el-icon-delete-solid"
              @click="delStock(scope.row)"
              >平仓</el-button>
          </el-row>
        </template>
      </el-table-column>
    </el-table>

    <el-row class="editAccount">
      <el-button type="primary" size="primary" @click="open2 = true; title2 = '新增持仓'">新增持仓</el-button>
    </el-row>

    <el-dialog :title="title" :visible.sync="open" width="60%" center>
      <el-form
        :model="stockChange"
        label-width=" 80px"
        ref="form"
      >
      <el-row>
        <el-col :span="12" >
          <el-form-item label="买入：" prop="addPosition" v-if="stockChange.mark == 1">
            <el-input v-model="stockChange.addPosition" placeholder="请输入买入股数" />
          </el-form-item>
          <el-form-item label="卖出：" prop="addPosition" v-if="stockChange.mark == -1">
            <el-input v-model="stockChange.addPosition" placeholder="请输入卖出股数" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="价格：" prop="addPrice">
            <el-input v-model="stockChange.addPrice" placeholder="请输入成交价" />
          </el-form-item>
        </el-col>
      </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="medium" @click="cancel">取消</el-button>
        <el-button size="medium" type="primary" @click="submitForm">确认</el-button>
      </span>
    </el-dialog>


    <el-dialog :title="title2" :visible.sync="open2" width="70%" center>
      <el-form
        :model="form"
        label-width=" 80px"
        ref="form"
      >
        <el-row>
          <el-col :span="12" >
            <el-form-item label="代码：">
              <el-input v-model="form.number" placeholder="请输入买入股票代码" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="名称：">
              <el-input v-model="form.name" placeholder="请输入买入股票名称" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12" >
            <el-form-item label="成本：">
              <el-input v-model="form.buy_price" placeholder="请输入买入成本" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="持仓数：">
              <el-input v-model="form.position" placeholder="请输入持仓数量" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="medium" @click="cancel">取消</el-button>
        <el-button size="medium" type="primary" @click="submitForm2">确认</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import { getStocks, deleteStock, updateStock, newStock } from '@/api/mystocks'

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
      title2: "",
      // 弹窗控制
      open: false,
      open2: false,
      // 持仓变动表
      stockChange: {},
      // 新增持仓
      form: {}
    }
  },
  created() {
    this.getList()
  },
  methods: { 
    // 获得表格显示数据
    getList() {
      getStocks().then(response => {
        this.tableData = response.stocks
      })
    },
    // 买入
    addStock(row) {
      this.reset();
      this.stockChange.oldbuy_price = row.buy_price,
      this.stockChange.old_position = row.position,
      this.stockChange.position = row.position,
      this.stockChange.id = row.id
      this.stockChange.mark = 1
      this.open = true
      this.title = "加，都可以加"
    },
    // 卖出
    sellStock(row) {
      this.reset();
      this.stockChange.oldbuy_price = row.buy_price,
      this.stockChange.old_position = row.position,
      this.stockChange.position = row.position,
      this.stockChange.id = row.id
      this.stockChange.mark = -1
      this.open = true
      this.title = "直接重仓空进去，%¥#，*&算了"

    },
    // 平仓
    delStock(row) {
      this.stockChange.id = row.id
      this.$confirm('确定要清仓' + row.name + '?', "警告", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning"
      }).then(() => {
        return deleteStock(row.id)
      }).then(response => {
          this.getList();
          // this.msgSuccess("删除成功");
        })
    },
    // 弹窗取消
    cancel() {
      this.open = false
      this.open2 = false
      this.reset();
      this.resetform();
    },
    // 弹窗提交
    submitForm: function() {
      const _this = this
      _this.stockChange.addPosition = parseFloat(_this.stockChange.addPosition)
      _this.stockChange.addPrice = parseFloat(_this.stockChange.addPrice)
      // console.log('_this.stockChange',_this.stockChange)
      if(_this.stockChange.mark == 1){
        _this.stockChange.position = _this.$math.add(_this.stockChange.old_position ,_this.stockChange.addPosition)
      }else{
        _this.stockChange.position = _this.$math.subtract(_this.stockChange.old_position ,_this.stockChange.addPosition)
      }
      _this.stockChange.buy_price = _this.newBuyPrice(_this.stockChange.old_position,_this.stockChange.oldbuy_price,_this.stockChange.addPosition,_this.stockChange.addPrice,_this.stockChange.mark)
      // console.log('sotckChange',_this.stockChange)
      if(_this.stockChange.mark == 1) {
            updateStock(_this.stockChange).then(response => {
              // _this.msgSuccess("买入成功");
              _this.open = false;
              _this.getList();
            });}
          else {
            updateStock(_this.stockChange).then(response => {
              // _this.msgSuccess("卖出成功");
              _this.open = false;
              _this.getList();
            })
          }
    },
    // 新增持仓弹窗提交按钮
    submitForm2: function() {
      const _this = this
      _this.form.price = 0
      _this.form.yest_price = 0
      newStock(_this.form).then(response => {
        // _this.msgSuccess("买入成功");
        _this.open2 = false;
        _this.getList();
      });
    },
    // 重制
    reset() {
      this.stockChange = {
        id: undefined,
        mark: undefined,
        addPosition: undefined,
        sellPosition: undefined,
        buy_price: undefined,
        addPrice: undefined,
        //原有信息
        oldbuy_price: undefined,
        old_position: undefined,
        position: undefined,
      };
    },
    // 重制新增表
    resetform() {
      this.form = {

      }
    },
    // 计算持有市值
    calculateMarketValue(a, b) {
      return a*b
    },
    // 计算个股盈亏
    calculateProfitValue(x, y, z){
      return (x-y)*z
    },
    // 保留两位小数
    fix2(num) {
      num = parseFloat(num).toFixed(2)
      return num
    },
    // 保留百分号并保留两位小数
    toPercent(point){
      let str=parseFloat(point*100).toFixed(2);
      str += "%";
      return str;
    },
    // 重新计算成本
    // newBuyPrice(op,on,np,nn,mark){
    //   let oldTotal = op * on
    //   if(mark == 1){      
    //     let tn = on + nn
    //     let newTotal = nn * np
    //     let newPrice = (newTotal + oldTotal) / tn
    //     return newPrice
    //   }else{
    //     let tn = on - nn
    //     let newTotal = nn * np
    //     let newPrice = (oldTotal - newTotal) / tn
    //     return newPrice
    //   }
    // }
    newBuyPrice(op,on,np,nn,mark){
      let oldTotal = this.$math.multiply(on,op)
      if(mark == 1){      
        let tn = this.$math.add(op,np)
        let newTotal = this.$math.multiply(nn,np)
        let newPrice = this.$math.divide(this.$math.add(newTotal,oldTotal),tn)
        return this.fix2(newPrice)
      }else{
        let tn = this.$math.subtract(op,np)
        let newTotal = this.$math.multiply(nn,np)
        let newPrice = this.$math.divide(this.$math.subtract(oldTotal,newTotal),tn)
        return this.fix2(newPrice)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.myaccount {
  padding: 32px;
}

.editAccount {
  margin-top: 40px;
}

.stocksTable {
  margin-top: 40px;
}
</style>
