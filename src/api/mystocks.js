import request from '@/utils/request'

export function getStocks() {
  return request({
    url: '/stock',
    method: 'get'
  })
}
