import request from '@/utils/request'

export function getStocks(query) {
  return request({
    url: '/stock',
    method: 'get'
  })
}
