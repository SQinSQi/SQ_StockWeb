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
              @click="sellStock(scope.row)"
              >平仓</el-button>
          </el-row>
        </template>
      </el-table-column>
    </el-table>

    <!-- <el-row class="editAccount">
      <el-button type="primary" size="primary" @click=addStock()>新增持仓</el-button>
    </el-row> -->

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
          <el-form-item label="价格：" prop="addprice">
            <el-input v-model="stockChange.addPrice" placeholder="请输入买入股价" />
          </el-form-item>
        </el-col>
      </el-row>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="medium" @click="cancel">取消</el-button>
        <el-button size="medium" type="primary" @click="submitForm">确认</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import { getStocks, deleteStock, updateStock } from '@/api/mystocks'

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
      stockChange: {},
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
      this.stockChange.id = row.id
      this.stockChange.mark = -1
      this.open = true
      this.title = "直接重仓空进去，%¥#，*&算了"

    },
    // 平仓
    deleteStock(row) {
      this.stockChange.id = row.id
      this.$confirm('确定要清仓' + row.name + '?', "警告", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning"
      })
        .then(function() {
          return deleteInfo(row.id);
        })
        .then(() => {
          this.getList();
          this.msgSuccess("删除成功");
        });
    },
    // 新增持仓
    newStock() {

    },
    // 弹窗取消
    cancel() {
      this.open = false
      this.reset();
    },
    // 弹窗提交
    submitForm: function() {
      // console.log(this.stockChange.oldbuy_price);
      // console.log(this.stockChange.old_position);
      // console.log(this.stockChange.addPrice);
      // console.log(this.stockChange.addPosition);
      this.stockChange.buy_price = this.newBuyPrice(this.stockChange.old_position,this.stockChange.oldbuy_price,this.stockChange.addPosition,this.stockChange.addPrice,this.stockChange.mark)
      // console.log(this.stockChange.buy_price);
      // let x = this.newBuyPrice(100,10,100,9,1)
      // console.log(x)
      if (this.stockChange.mark == 1) {
            updateStock(this.stockChange).then(response => {
              this.msgSuccess("买入成功");
              this.open = false;
              this.getList();
            });}
          else {
            updateStock(this.stockChange).then(response => {
              this.msgSuccess("卖出成功");
              this.open = false;
              this.getList();
            })
          }
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
      };
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
      num = num.toFixed(2)
      return num
    },
    // 保留百分号并保留两位小数
    toPercent(point){
      let str=Number(point*100).toFixed(2);
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
      console.log('oldtotal:',oldTotal)
      if(mark == 1){      
        let tn = this.$math.add(on,nn)
        console.log('tn:',tn)
        let newTotal = this.$math.multiply(nn,np)
        console.log('newTotal:', newTotal)
        let newPrice = this.$math.divide(this.$math.add(newTotal,oldTotal),tn)
        console.log('newPrice:',newPrice)
        return newPrice
      }else{
        let tn = this.$math.subtract(on,nn)
        let newTotal = this.$math.multiply(nn,np)
        let newPrice = this.$math.divide(this.$math.subtract(oldTotal,newTotal),tn)
        return newPrice
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
