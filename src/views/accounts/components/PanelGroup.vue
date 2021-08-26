<template>
  <div class="card-panel">
    <el-row class="card-panel-up">
      <div class="card-panel-upleft">
        <div class="card-panel-text-upleft">
          <span>总资产（人民币）</span>
        </div>
        <div class="card-panel-assetsnum">
          <span>{{this.calculateData.totalMarket}}</span>
        </div>
      </div>
      <div class="card-panel-upright">
        <div class="card-panel-text-upright">
          <span>今日盈亏</span>
        </div>
        <div class="card-panel-assetschange">
          <span id="changeup">{{this.calculateData.todayProfit}}</span>
          <span id="changedown">{{this.calculateData.todayProfitPercet}}</span>
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
        <span class="card-panel-text-down">{{this.calculateData.totalProfit}}</span>
      </div>
      <div class="card-panel-text-3">
        <span class="card-panel-text-down">盈利:</span>
        <span class="card-panel-text-down">{{this.calculateData.totalProfitPercent}}</span>
      </div>
    </el-row>
  </div>
</template>

<script>
import { getStocks } from '@/api/mystocks'

export default {
  data() {
    return{
      stocksData:[],
      calculateData:{
        totalMarket:"",
        totalProfit:"",
        totalProfitPercent:"",
        todayProfit:"",
        todayProfitPercet:""
      },
      teststocks: [
        {
          "buy_price": 50.363, 
          "id": 1.0, 
          "name": "\u62db\u5546\u94f6\u884c", 
          "number": "600036", 
          "position": 28100.0, 
          "price": 49.85,
          "yest_price":50.11
        }, 
        {
          "buy_price": 54.979, 
          "id": 2.0, 
          "name": "\u4e2d\u56fd\u5e73\u5b89", 
          "number": "601318", 
          "position": 600.0, 
          "price": 50.48,
          "yest_price":50.11
        }, 
        {
          "buy_price": 35.535, 
          "id": 3.0, 
          "name": "\u817e\u8baf\u63a7\u80a1", 
          "number": "002142", 
          "position": 7700.0, 
          "price": 32.79,
          "yest_price":34.11
        },
        {
          "buy_price": 21.433, 
          "id": 4.0, 
          "name": "\u817e\u8baf\u63a7\u80a1", 
          "number": "002142", 
          "position": 1500.0, 
          "price": 18.69,
          "yest_price":20.11
        }
      ]
    }
  },
  created() {
    this.getAllStocks()
    this.getTotal(this.stocksData)
  },
  methods: {
    // 获得股票数据
    getAllStocks() {
      getStocks().then(response => {
        this.stocksData = response.stocks
      })
    },
    // 计算总市值
    getTotal(stocksData) {
      let sum = 0
      let sum_profit = 0
      let sum_cost = 0
      let sum_yesterday = 0
      stocksData.forEach(item => {
        let Market = this.calculateMarketValue(item.position,item.price)
        let cost = this.calculateMarketValue(item.buy_price,item.position)
        let yesterdayMarket = this.calculateMarketValue(item.yest_price,item.position)
        sum_cost += cost
        sum += Market
        sum_yesterday += yesterdayMarket
      })
      stocksData.forEach(item => {
        let Profit = this.calculateProfitValue(item.price,item.buy_price,item.position)
        sum_profit += Profit
      })
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
