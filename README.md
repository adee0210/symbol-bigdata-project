# A. DATA SOURCE

Tài liệu mô tả chi tiết các nguồn dữ liệu realtime crypto và cấu trúc bảng lưu trữ tương ứng.  
Nguồn chủ yếu từ CoinMarketCap và Binance (Spot & Futures), ngoài ra có thêm TradingView (Dominance).

---

## 1. CoinMarketCapData

### Nguồn dữ liệu
- Nguồn: https://pro.coinmarketcap.com/account/
- API key: 
- Giới hạn: 10,000 request/tháng (gói Free)
- Loại: Realtime / Update per second

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Ký hiệu đồng coin (BTC, ETH, ...) |
| name | varchar | Tên đầy đủ của đồng coin |
| datetime | datetime | Thời điểm lấy dữ liệu |
| price | float | Giá hiện tại (USD) |
| cmc_rank | int | Thứ hạng trên CMC |
| change_1h_percent | float | % thay đổi trong 1 giờ |
| change_24h_percent | float | % thay đổi trong 24 giờ |
| change_7d_percent | float | % thay đổi trong 7 ngày |
| volume | float | Khối lượng giao dịch gần nhất |
| market_cap | float | Vốn hóa thị trường |
| volume_24h | float | Tổng volume 24h |
| circulating_supply | float | Số lượng coin lưu hành |

---

## 2. Trade

### Nguồn dữ liệu
- WebSocket: `wss://stream.binance.com:9443/ws/btcusdt@trade`
- Mỗi stream = 1 cặp giao dịch (`symbol` viết thường + `usdt`)
- Giới hạn: tối đa 1024 stream/connection

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Cặp giao dịch |
| price | float | Giá khớp lệnh |
| trade_time | datetime | Thời điểm giao dịch |
| quantity | float | Khối lượng coin giao dịch |
| maker | bool | Người tạo lệnh (true nếu là maker) |

---

## 3. Depth

### Nguồn dữ liệu
- WebSocket: `wss://stream.binance.com:9443/ws/btcusdt@depth`
- Cập nhật realtime orderbook (bid/ask)

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Cặp giao dịch |
| side | varchar | Loại lệnh: `bid` hoặc `ask` |
| price | decimal | Giá chào mua/bán |
| quantity | decimal | Khối lượng tại mức giá đó |
| amount_total | decimal | Tổng khối lượng tích lũy |
| updated_at | timestamp | Thời điểm cập nhật orderbook |

---

## 4. Kline

### Nguồn dữ liệu
- WebSocket: `wss://stream.binance.com:9443/ws/btcusdt@kline_1m`
- Dữ liệu nến (OHLCV) theo khung thời gian (1m, 1h, 1d,...)

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| id | bigint | ID tự tăng |
| symbol | varchar | Cặp giao dịch |
| interval | varchar | Khung thời gian (1m, 5m, 1h, 1d, …) |
| open_time | timestamp | Thời gian mở nến |
| open | decimal | Giá mở |
| high | decimal | Giá cao nhất |
| low | decimal | Giá thấp nhất |
| close | decimal | Giá đóng |
| volume | decimal | Khối lượng giao dịch |
| close_time | timestamp | Thời gian đóng nến |

---

## 5. Dominance

### Nguồn dữ liệu
- Source: TradingView (CRYPTOCAP)
- Ví dụ symbol:
  - `CRYPTOCAP:BTC.D` → BTC Dominance  
  - `CRYPTOCAP:ETH.D` → ETH Dominance  
  - `CRYPTOCAP:TOTAL` → Tổng vốn hóa thị trường  
- Thư viện Python: `tvDatafeed`
- Tần suất: tùy chọn (1h, 4h, 1d...)

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Mã chỉ số (BTC.D, ETH.D, ...) |
| open | float | Giá mở đầu kỳ |
| high | float | Giá cao nhất |
| low | float | Giá thấp nhất |
| close | float | Giá đóng |
| volume | float | Khối lượng (thường = 0) |
| type | varchar | Loại dữ liệu (dominance, total_market, …) |
| datetime | datetime | Thời điểm ghi nhận |

---

## 6. funding_rate

### Nguồn dữ liệu
- WebSocket: `wss://fstream.binance.com/ws/btcusdt@fundingRate`
- Cập nhật: mỗi 8h/lần

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Cặp giao dịch |
| funding_rate | decimal | Tỷ lệ tài trợ (Funding Rate) |
| funding_time | timestamp | Thời điểm funding hiện tại |
| mark_price | decimal | Giá mark |
| index_price | decimal | Giá index |
| type | varchar | Loại hợp đồng (perpetual, quarterly, …) |
| next_funding_time | timestamp | Lần funding kế tiếp |

---

## 7. Liquidation

### Nguồn dữ liệu
- WebSocket: `wss://fstream.binance.com/ws/btcusdt@forceOrder`
- Cập nhật: realtime mỗi khi có lệnh bị thanh lý

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Cặp giao dịch |
| price | decimal | Giá thanh lý |
| quantity | decimal | Khối lượng bị thanh lý |
| side | varchar | Hướng lệnh: `BUY` hoặc `SELL` |
| time | timestamp | Thời điểm thanh lý |

---

## 8. exchange_info

### Nguồn dữ liệu
- REST API: `https://api.binance.com/api/v3/exchangeInfo`
- Cung cấp thông tin chung của sàn

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| exchange_name | varchar | Tên sàn (Binance, OKX, …) |
| timezone | varchar | Múi giờ hoạt động |
| datetime | timestamp | Thời điểm đồng bộ dữ liệu |

---

## 9. open_interest

### Nguồn dữ liệu
- REST API: `https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT`
- Hoặc WebSocket: `wss://fstream.binance.com/ws/btcusdt@openInterest`

### Ý nghĩa dữ liệu

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| symbol | varchar | Cặp giao dịch |
| open_interest | decimal | Tổng hợp đồng mở |
| timestamp | timestamp | Thời điểm ghi nhận |

---

### DBML STRUCTURE

```dbml
// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table Trade {
  symbol varchar
  price float
  trade_time datetime
  quantity float
  maker bool
}

Table Depth {
  symbol varchar
  side varchar
  price decimal
  quantity decimal
  amount_total decimal
  updated_at timestamp
}

Table CoinMarketCapData {
  symbol varchar
  name varchar
  datetime datetime
  price float
  cmc_rank int
  change_1h_percent float
  change_24h_percent float
  change_7d_percent float
  volume float
  market_cap float
  volume_24h float
  circulating_supply float
}

Table Dominance {
  symbol varchar
  open float
  high float
  low float
  close float
  volume float
  type varchar
  datetime datetime
}

Table funding_rate {
  symbol varchar          
  funding_rate decimal    
  funding_time timestamp 
  mark_price decimal      
  index_price decimal     
  type varchar
  next_funding_time timestamp 
}

Table Kline {
  id bigint
  symbol varchar
  interval varchar
  open_time timestamp
  open decimal
  high decimal
  low decimal
  close decimal
  volume decimal
  close_time timestamp
}

Table Liquidation {
  symbol varchar
  price decimal
  quantity decimal
  side varchar
  time timestamp
}

Table exchange_info {
  exchange_name varchar
  timezone varchar
  datetime timestamp
}

Table open_interest {
  symbol varchar
  open_interest decimal
  timestamp timestamp
}
# symbol-bigdata-project
