<template>
  <div class="card-panel">
    <el-row class="card-panel-up">
      <div class="card-panel-upleft">
        <div class="card-panel-text-upleft">
          <span>总资产（人民币）</span>
        </div>
        <div class="card-panel-assetsnum">
          <span>21W</span>
        </div>
      </div>
      <div class="card-panel-upright">
        <div class="card-panel-text-upright">
          <span>今日盈亏</span>
        </div>
        <div class="card-panel-assetschange">
          <span id="changeup">23856.54</span>
          <span id="changedown">-2.68%</span>
        </div>
      </div>
    </el-row>
    <el-row class="card-panel-mid">
      <div class="card-panel-line" />
    </el-row>
    <el-row class="card-panel-down">
      <div class="card-panel-down-1">
        <span class="card-panel-text-down">持有市值:</span>
        <span class="card-panel-text-down">219150</span>
      </div>
      <div class="card-panel-down-2">
        <span class="card-panel-text-down">浮动盈亏:</span>
        <span class="card-panel-text-down">11329.26</span>
      </div>
      <div class="card-panel-text-3">
        <span class="card-panel-text-down">盈利:</span>
        <span class="card-panel-text-down">22.36%</span>
      </div>
    </el-row>
  </div>
</template>

<script>
import { getStocks } from '@/api/mystocks'

export default {
  data() {
    return{
      stocksData:{}
    }
  },
  created() {
    getAllStocks()
  },
  methods: {
    // 获得股票数据
    getAllStocks() {
      getStocks().then(response => {
        this.stocksData = response.stocks
      })
    },
    // 计算总市值
    getTotal() {
      

    } 
    // 计算当日盈亏

    // 计算当日盈亏比
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
    .card-panel-down-1 {
      display: flex;
      flex-wrap: wrap;
    }
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
