<template>
  <div class="card-panel">
    <el-row class="card-panel-up">
      <div class="card-panel-upleft">
        <div class="card-panel-text-upleft">
          <span>总资产（人民币）</span>
        </div>
        <div class="card-panel-assetsnum">
          <span>{{fix2(this.calculateData.totalMarket)}}</span>
        </div>
      </div>
      <div class="card-panel-upright">
        <div class="card-panel-text-upright">
          <span>今日盈亏</span>
        </div>
        <div class="card-panel-assetschange">
          <span id="changeup">{{fix2(this.calculateData.todayProfit)}}</span>
          <span id="changedown">{{toPercent(this.calculateData.todayProfitPercet)}}</span>
        </div>
      </div>
    </el-row>
    <el-row class="card-panel-mid">
      <div class="card-panel-line" />
    </el-row>
    <el-row class="card-panel-down">
      <!-- <div class="card-panel-down-1">
        <span class="card-panel-text-down">持有市值:</span>
        <span class="card-panel-text-down">{{this.caculateData.totalMarket}}</span>
      </div> -->
      <div class="card-panel-down-2">
        <span class="card-panel-text-down">浮动盈亏:</span>
        <span class="card-panel-text-down">{{fix2(this.calculateData.totalProfit)}}</span>
      </div>
      <div class="card-panel-text-3">
        <span class="card-panel-text-down">盈利:</span>
        <span class="card-panel-text-down">{{toPercent(this.calculateData.totalProfitPercent)}}</span>
      </div>
    </el-row>
  </div>
</template>

<script>
import { getStocks } from '@/api/mystocks'


var num =2.446242342;
num = num.toFixed(2);
console.log(num); 
export default {
  data() {
    return{
      stocksData: [],
      calculateData:{
        totalMarket:"",
        totalProfit:"",
        totalProfitPercent:"",
        todayProfit:"",
        todayProfitPercet:""
      },
    }
  },
  created() {
    this.getAllStocks()
  },
  methods: {
    // 获得股票数据
    getAllStocks() {
      getStocks().then(response => {       
        this.stocksData = response.stocks;
        this.getTotal(response.stocks)
      })
    },
    // 计算总市值
    getTotal(stocksInfo) {
      let obj = stocksInfo
      let sum = 0
      let sum_profit = 0
      let sum_cost = 0
      let sum_yesterday = 0
      for(var i in obj) {
        let Market = this.calculateMarketValue(obj[i].position,obj[i].price)
        let cost = this.calculateMarketValue(obj[i].buy_price,obj[i].position)
        let yesterdayMarket = this.calculateMarketValue(obj[i].yest_price,obj[i].position)
        sum_cost += cost
        sum += Market
        sum_yesterday += yesterdayMarket
      }
      for(var j in obj) {      
        let Profit = this.calculateProfitValue(obj[j].price,obj[j].buy_price,obj[j].position)
        sum_profit += Profit
      }
      this.calculateData.totalMarket = sum
      this.calculateData.totalProfit = sum_profit
      this.calculateData.totalProfitPercent = this.calculateProfitPercet(sum_cost,sum_profit)
      this.calculateData.todayProfit = sum - sum_yesterday
      this.calculateData.todayProfitPercet = this.calculateData.todayProfit / sum_yesterday
    },
    // 计算持有市值
    calculateMarketValue(a, b) {
      return a*b
    },
    // 计算盈亏
    calculateProfitValue(x, y, z){
      return (x-y)*z
    },
    // 计算盈亏百分比
    calculateProfitPercet(x, y){
      return y/x
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
    }
  }
}
</script>


<style lang="scss" scoped>
.card-panel {
  display: flex;
  flex-wrap: wrap;
  margin-top: 2vh;
  margin-bottom: 2vh;
  height: 216px;
  position: relative;
  overflow: hidden;
  border-radius: 25px;
  background: #197278;
  color: white;

  .card-panel-up {
    flex: 0 0 100%;
    display: flex;
    .card-panel-upleft{
      flex: 1 0 300px;
      padding: 20px;
      .card-panel-text-upleft {
        font-weight: bold;
        font-size: 20px;
        padding-bottom: 20px;
      }
      .card-panel-assetsnum{
        padding: 2px;
        font-size: 40px;
        font-weight: bold;
      }
    }
    .card-panel-upright{
      padding: 20px;
      flex: 1 0 100px;
      text-align: right;
      .card-panel-text-upright {
        padding: 5px;
        font-size: 18px;
        font-weight: bold;
      }
      .card-panel-assetschange {
        padding: 5px;
        font-size: 18px;
        font-weight: bold;
        display: flex;
        flex-wrap: wrap;
        #changeup {
          padding: 2px;
          flex: 0 0 100%;
        }
        #changedown {
          padding: 2px;
          flex: 0 0 100%;
        }
      }
    }
  }

  .card-panel-mid {
    flex: 0 0 100%;
    .card-panel-line {
      width: 100%;
      height: 1px;
      border-top: solid #fffbff 1px;
      }
  }

  .card-panel-down {
    flex: 0 0 100%;
    display: flex;
    justify-content: space-around;
    // .card-panel-down-1 {
    //   display: flex;
    //   flex-wrap: wrap;
    // }
    .card-pannel-down-2 {
      display: flex;
      flex-wrap: wrap;
    }
    .card-pannel-down-3 {
      display: flex;
      flex-wrap: wrap;
    }
    .card-panel-text-down {
      padding-right: 1vw;
      padding-left: 1vw;
      font-weight: bold;
      font-size: 1.4vw;
    }
  }
}
</style>
