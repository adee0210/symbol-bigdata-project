# I. DATA SOURCE

## A. DỮ LIỆU CHỨNG KHOÁN VIỆT NAM

**Thời gian giao dịch cổ phiếu, ETF (HOSE, HNX, UPCoM):**

| Phiên | Thời gian | Ghi chú |
|-------|-----------|---------|
| Khớp lệnh định kỳ mở cửa (ATO) | 9:00 – 9:15 | Xác định giá mở cửa |
| Khớp lệnh liên tục | 9:15 – 11:30 | Giao dịch theo giá thỏa thuận giữa mua và bán |
| Nghỉ trưa | 11:30 – 13:00 | Không giao dịch |
| Khớp lệnh liên tục buổi chiều | 13:00 – 14:30 (HOSE), 13:00 – 15:00 (HNX/UPCoM) | Giao dịch bình thường |
| Khớp lệnh định kỳ đóng cửa (ATC) | 14:30 – 14:45 (HOSE), 15:00 – 15:05 (HNX/UPCoM) | Xác định giá đóng cửa |

**Lưu ý:**

-   **ATO (At The Open)**: Giá mở cửa, lệnh được khớp theo giá xác định.
-   **ATC (At The Close)**: Giá đóng cửa, lệnh được khớp theo giá xác định.
-   **Khớp lệnh liên tục**: Giá thay đổi theo cung-cầu từng phút.

**Thời gian giao dịch phái sinh (Index Futures VN30):**

| Phiên | Thời gian |
|-------|-----------|
| Sáng | 9:00 – 11:30 |
| Chiều | 13:00 – 15:00 |

### 1) Candlestick Data

-   Các data source sẽ được lấy theo timeframe là theo 1 phút (1m) sẽ được crawl theo lịch sử và realtime bao gồm:
    
    -   **Mã cổ phiếu (Stocks) hay Cổ phiếu gồm:**

        -   **Ngân hàng**

            | Mã | Công ty |
            |----|--------|
            | VCB | Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank) |
            | BID | Ngân hàng TMCP Đầu tư và Phát triển Việt Nam (BIDV) |
            | CTG | Ngân hàng TMCP Công thương Việt Nam (VietinBank) |
            | TPB | Ngân hàng TMCP Tiên Phong (TPBank) |
            | MBB | Ngân hàng Quân đội (MB Bank) |
            | ACB | Ngân hàng Á Châu |
            | SHB | Ngân hàng TMCP Sài Gòn - Hà Nội |
            | VPB | Ngân hàng TMCP Việt Nam Thịnh Vượng |
            | TCB | Ngân hàng TMCP Kỹ thương Việt Nam |

        -   **Bất động sản**

            | Mã | Công ty |
            |----|--------|
            | VHM | Vinhomes |
            | NVL | Novaland |
            | HDG | Tập đoàn Hà Đô |
            | DXG | Đất Xanh Group |
            | KDH | Địa ốc Khang Điền |
            | BCM | Tập đoàn Becamex IDC |
            | PDR | Phát triển Bất động sản Phát Đạt |

        -   **Công nghiệp & Thép**

            | Mã | Công ty |
            |----|--------|
            | HPG | Tập đoàn Hòa Phát |
            | NKG | Thép Nam Kim |
            | HSG | Tôn Hoa Sen |
            | VIC | Tập đoàn Vingroup (công nghiệp, bất động sản, bán lẻ) |
            | DHC | Công ty Cổ phần Đông Hải Bến Tre |

        -   **Tiêu dùng & Thực phẩm**

            | Mã | Công ty |
            |----|--------|
            | VNM | Vinamilk |
            | MWG | Thế Giới Di Động |
            | PNJ | Vàng bạc PNJ |
            | MSN | Tập đoàn Masan |
            | SAB | Sabeco |

        -   **Dịch vụ & Viễn thông**

            | Mã | Công ty |
            |----|--------|
            | FPT | FPT Corporation |
            | VGI | VGI Holdings (Quảng cáo, logistics) |
            | VTP | Viettel Post (trên UPCoM) |
            | GAS | PV Gas |
            | VJC | Vietjet Air |
            | HVN | Vietnam Airlines |

        -   **Vận tải**

            | Mã | Công ty |
            |----|--------|
            | GMD | |
            | VSC | |
            | HAH | |
            | VOS | |
            | PVT | |
            | VNS | |
            | VTO | |
            | SGN | |

        -   **Nguyên vật liệu (Thép, VLXD)**

            | Mã | Công ty |
            |----|--------|
            | HPG | Tập đoàn Hòa Phát |
            | HSG | Tôn Hoa Sen |
            | NKG | Thép Nam Kim |
            | DHC | Công ty Cổ phần Đông Hải Bến Tre |
            | POM | |
            | SMC | |
            | TVN | |
            | TLH | |
            | VIS | |

        -   **Thực phẩm & Đồ uống**

            | Mã | Công ty |
            |----|--------|
            | VNM | Vinamilk |
            | SAB | Sabeco |
            | MSN | Tập đoàn Masan |
            | KDC | |
            | BHN | |
            | QNS | |
            | SBT | |
            | PAN | |
            | VCF | |

        -   **Hàng hóa công nghiệp**

            | Mã | Công ty |
            |----|--------|
            | PVS | |
            | PVC | |
            | HAX | |
            | PVD | |
            | PTL | |
            | PCS | |
            | VPG | |
            | BWE | |

        -   **Tiện ích**

            | Mã | Công ty |
            |----|--------|
            | REE | |
            | PPC | |
            | NT2 | |
            | POW | PetroVietnam Power |
            | PGV | |
            | CHP | |
            | SJD | |
            | TMP | |

        -   **Viễn thông / CNTT**

            | Mã | Công ty |
            |----|--------|
            | VGI | VGI Holdings (Quảng cáo, logistics) |
            | FPT | FPT Corporation |
            | CMG | |
            | FOX | |
            | CTR | |
            | ABC | |
            | VTC | |

        -   **Phân phối & Bán lẻ**

            | Mã | Công ty |
            |----|--------|
            | MWG | Thế Giới Di Động |
            | DGW | |
            | FRT | |
            | PET | |
            | AST | |
            | BSR | Binh Son Refining |
            | PIT | |

        -   **Phần mềm**

            | Mã | Công ty |
            |----|--------|
            | FPT | FPT Corporation |
            | CMG | |
            | CMC | |
            | ITD | |
            | SRA | |
            | ELC | |
            | ADT | |
            | ONE | |

        -   **Dịch vụ tài chính (Chứng khoán)**

            | Mã | Công ty |
            |----|--------|
            | SSI | |
            | HCM | |
            | VND | |
            | VCI | |
            | BSI | |
            | VIX | |
            | MBS | |
            | CTS | |

        -   **Năng lượng**

            | Mã | Công ty |
            |----|--------|
            | GAS | PV Gas |
            | POW | PetroVietnam Power |
            | PLX | |
            | BSR | Binh Son Refining |
            | PGD | |
            | OIL | |
            | PC1 | |
            | PVG | |

        -   **Hàng tiêu dùng**

            | Mã | Công ty |
            |----|--------|
            | MSN | Tập đoàn Masan |
            | KDC | |
            | VNM | Vinamilk |
            | BHN | |
            | QNS | |
            | PAN | |
            | LSS | |

        -   **Bảo hiểm**

            | Mã | Công ty |
            |----|--------|
            | BVH | |
            | PVI | |
            | MIG | |
            | BMI | |
            | BIC | |
            | PTI | |
            | ABI | |
            | PRE | |

        -   **Dược phẩm**

            | Mã | Công ty |
            |----|--------|
            | DHG | |
            | TRA | |
            | IMP | |
            | DMC | |
            | DBD | |
            | MKP | |
            | OPC | |
            | PME | |

        -   **Dịch vụ tiêu dùng / Trang sức**

            | Mã | Công ty |
            |----|--------|
            | PNJ | Vàng bạc PNJ |
            | HPG | Tập đoàn Hòa Phát |
            | MWG | Thế Giới Di Động |
            | SCS | |
            | VJC | Vietjet Air |
            | HVN | Vietnam Airlines |
            | AST | |

        -   **Dịch vụ thương mại**

            | Mã | Công ty |
            |----|--------|
            | MWG | Thế Giới Di Động |
            | PNJ | Vàng bạc PNJ |
            | VRE | |
            | DGW | |
            | PET | |
            | PIT | |
            | AMD | |

        -   **Ô tô & Linh kiện**

            | Mã | Công ty |
            |----|--------|
            | HAX | |
            | TCH | |
            | TMT | |
            | DRC | |
            | SRC | |
            | CSM | |
            | HHS | |
            | SVC | |

        -   **Truyền thông & Giải trí**

            | Mã | Công ty |
            |----|--------|
            | VGI | VGI Holdings (Quảng cáo, logistics) |
            | FPT | FPT Corporation |
            | CMG | |
            | VNG | |
            | YEG | |
            | EBS | |
            | ADS | |
            | VTP | |

        -   **Dịch vụ chăm sóc sức khỏe**

            | Mã | Công ty |
            |----|--------|
            | MED | |
            | DHC | Công ty Cổ phần Đông Hải Bến Tre |
            | DBD | |
            | TNH | |
            | VMD | |
            | DVN | |
            | FIT | |
            | JVC | |

        -   **Đồ gia dụng**

            | Mã | Công ty |
            |----|--------|
            | MWG | Thế Giới Di Động |
            | REE | |
            | GDT | |
            | RAL | |
            | TLG | |
            | PAC | |
            | SHA | |

        -   **Phần cứng**

            | Mã | Công ty |
            |----|--------|
            | FPT | FPT Corporation |
            | CMC | |
            | CMG | |
            | GEX | |
            | DGW | |
            | VNZ | |
            | DNC | |
            | ITD | |

    -   **Mã chỉ số (Index) hay Chỉ số chứng khoán:** VN INDEX, VN30 INDEX, VN100 INDEX, HNX INDEX
        
    -   **Mã ETF (ETF Tickers) hay Mã quỹ ETF gồm các mã hỗ trợ:** E1VFVN30, FUEABVND, FUEBFVND, FUECMID, FUEFCV50, FUEIP100, FUEKIV30, FUEKIVFS, FUEKIVND, FUEMAV30, FUEMAVND, FUESSV30, FUESSV50, FUESSVFL, FUETC50, FUETPVND, FUEVFVND, FUEVN100
        
    -   **Mã Phái sinh (Derivatives) gồm Hợp đồng tương lai chỉ số (Index Futures) và Hợp đồng tương lai trái phiếu bao gồm:** VN30F*, GB05F*, GB10F*
        
-   **Các trường sẽ được lấy bao gồm:**
    
    | Trường | Kiểu dữ liệu |
    |--------|--------------|
    | symbol | str |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS |
    | open | float |
    | high | float |
    | low | float |
    | close | float |
    | volume | float |
    

### 2) Trade Data

-   Dữ liệu giao dịch sẽ được lấy theo realtime cho các mã cổ phiếu, chỉ số, ETF và phái sinh đã liệt kê ở trên.
    
-   **Các trường sẽ được lấy bao gồm(riêng phái sinh sẽ có thêm trường mua bán):**
    
    | Trường | Kiểu dữ liệu |
    |--------|--------------|
    | symbol | str |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS |
    | volume | float |
    | price | float |
    | change | float |
    | M/B | str |


### 3) Orderbook Data

-   Dữ liệu giao dịch sẽ được lấy theo realtime cho các mã cổ phiếu, chỉ số, ETF và phái sinh đã liệt kê ở trên.


-   **Các trường sẽ được lấy bao gồm:**
    

## B. DỮ LIỆU CRYPTO

### 1) Trade
*Dữ liệu các giao dịch khớp lệnh trên sàn, ghi lại từng lần mua/bán thực tế.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| price | float |
| trade_time | datetime |
| quantity | float |
| maker | bool |

### 2) Depth
*Dữ liệu sổ lệnh (Orderbook), thể hiện các mức giá và khối lượng đặt mua/bán tại từng thời điểm.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| side | varchar |
| price | decimal |
| quantity | decimal |
| amount_total | decimal |
| updated_at | timestamp |

### 3) CoinMarketCapData
*Dữ liệu tổng hợp từ CoinMarketCap, gồm giá, vốn hóa, khối lượng, thứ hạng và các chỉ số biến động của đồng coin.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| name | varchar |
| datetime | datetime |
| price | float |
| cmc_rank | int |
| change_1h_percent | float |
| change_24h_percent | float |
| change_7d_percent | float |
| volume | float |
| market_cap | float |
| volume_24h | float |
| circulating_supply | float |

### 4) Dominance
*Dữ liệu thể hiện tỷ trọng (dominance) của một đồng coin so với toàn thị trường, gồm giá mở, cao, thấp, đóng và khối lượng.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| open | float |
| high | float |
| low | float |
| close | float |
| volume | float |
| type | varchar |
| datetime | datetime |

### 5) funding_rate
*Dữ liệu funding rate (lãi suất qua đêm) của các hợp đồng phái sinh, gồm giá, thời gian, loại hợp đồng và các chỉ số liên quan.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| funding_rate | decimal |
| funding_time | timestamp |
| mark_price | decimal |
| index_price | decimal |
| type | varchar |
| next_funding_time | timestamp |

### 6) Kline
*Dữ liệu nến (Kline/Candlestick), gồm giá mở, cao, thấp, đóng, khối lượng và thời gian cho từng khung thời gian.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| interval | varchar |
| open_time | timestamp |
| open | decimal |
| high | decimal |
| low | decimal |
| close | decimal |
| volume | decimal |
| close_time | timestamp |

### 7) Liquidation
*Dữ liệu các lệnh thanh lý (liquidation) trên thị trường phái sinh, gồm giá, khối lượng, chiều lệnh và thời gian.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| price | decimal |
| quantity | decimal |
| side | varchar |
| time | timestamp |

### 8) exchange_info
*Thông tin về sàn giao dịch, múi giờ và thời điểm cập nhật.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| exchange_name | varchar |
| timezone | varchar |
| datetime | timestamp |

### 9) open_interest
*Dữ liệu open interest (khối lượng hợp đồng mở) của các hợp đồng phái sinh tại từng thời điểm.*
| Trường | Kiểu dữ liệu |
|--------|--------------|
| symbol | varchar |
| open_interest | decimal |
| timestamp | timestamp |