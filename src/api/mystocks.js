import request from '@/utils/request'

export function getStocks() {
  return request({
    url: '/stock/',
    method: 'get'
  })
}

export function updateStock(stockchange) {
  return request({
    url: '/stock/' + stockchange.id,
    method: 'put',
    data: stockchange
  })
}