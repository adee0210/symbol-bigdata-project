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
            | VNM | Công ty Cổ phần Sữa Việt Nam (Vinamilk) |
            | MWG | Thế Giới Di Động |
            | PNJ | Vàng bạc PNJ |
            | MSN | Tập đoàn Masan |
            | SAB | Tổng Công ty Cổ phần Bia - Rượu - Nước giải khát Sài Gòn (Sabeco) |
            | KDC | Công ty Cổ phần Thực phẩm Kinh Đô |
            | BHN | Tổng Công ty Cổ phần Bia Hà Nội |
            | QNS | Công ty Cổ phần Đường Quảng Ngãi |
            | SBT | Công ty Cổ phần Thành Thành Công - Biên Hòa |
            | PAN | Công ty Cổ phần Tập đoàn PAN |
            | VCF | Công ty Cổ phần Vinacafe Biên Hòa |

        -   **Dịch vụ & Viễn thông**

            | Mã | Công ty |
            |----|--------|
            | FPT | FPT Corporation |
            | VGI | Công ty Cổ phần Đầu tư Quốc tế Viettel |
            | VTP | Viettel Post (trên UPCoM) |
            | GAS | PV Gas |
            | VJC | Vietjet Air |
            | HVN | Vietnam Airlines |

        -   **Vận tải**

            | Mã  | Công ty |
            |-----|-------------------------------------------------------------|
            | GMD | Công ty Cổ phần Gemadept |
            | VSC | Công ty Cổ phần Container Việt Nam |
            | HAH | Công ty Cổ phần Vận tải và Xếp dỡ Hải An |
            | VOS | Công ty Cổ phần Vận tải biển Việt Nam |
            | PVT | Tổng Công ty Cổ phần Vận tải Dầu khí |
            | VNS | Công ty Cổ phần Ánh Dương Việt Nam |
            | VTO | Công ty Cổ phần Vận tải Xăng dầu Vitaco |
            | SGN | Công ty Cổ phần Phục vụ Mặt đất Sài Gòn |

        -   **Nguyên vật liệu (Thép, VLXD)**

            | Mã  | Công ty |
            |-----|-------------------------------------------------------------|
            | HPG | Tập đoàn Hòa Phát |
            | HSG | Công ty Cổ phần Tập đoàn Hoa Sen |
            | NKG | Công ty Cổ phần Thép Nam Kim |
            | DHC | Công ty Cổ phần Đông Hải Bến Tre |
            | POM | Công ty Cổ phần Thép Pomina |
            | SMC | Công ty Cổ phần Đầu tư Thương mại SMC |
            | TVN | Công ty Cổ phần Thép Việt Nam |
            | TLH | Công ty Cổ phần Tập đoàn Thép Tiến Lên |
            | VIS | Công ty Cổ phần Thép Việt Ý |

        -   **Thực phẩm & Đồ uống**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | VNM | Công ty Cổ phần Sữa Việt Nam (Vinamilk) |
            | SAB | Tổng Công ty Cổ phần Bia - Rượu - Nước giải khát Sài Gòn (Sabeco) |
            | MSN | Công ty Cổ phần Tập đoàn Masan |
            | KDC | Công ty Cổ phần Thực phẩm Kinh Đô |
            | BHN | Tổng Công ty Cổ phần Bia Hà Nội |
            | QNS | Công ty Cổ phần Đường Quảng Ngãi |
            | SBT | Công ty Cổ phần Thành Thành Công - Biên Hòa |
            | PAN | Công ty Cổ phần Tập đoàn PAN |
            | VCF | Công ty Cổ phần Vinacafe Biên Hòa |

        -   **Hàng hóa công nghiệp**

            | Mã  | Công ty |
            |-----|-------------------------------------------------------------|
            | PVS | Tổng Công ty Cổ phần Dịch vụ Kỹ thuật Dầu khí Việt Nam |
            | PVC | Tổng Công ty Dung dịch khoan và Hóa phẩm Dầu khí |
            | HAX | Công ty Cổ phần Dịch vụ Ô tô Hàng Xanh |
            | PVD | Tổng Công ty Cổ phần Khoan và Dịch vụ Dầu khí |
            | PTL | Công ty Cổ phần Đầu tư và Xây dựng Dầu khí PETROLAND |
            | PCS | Công ty Cổ phần Dịch vụ Vận tải và Thương mại |
            | VPG | Công ty Cổ phần Sản xuất và Thương mại Việt Phát |
            | BWE | Công ty Cổ phần Nước - Môi trường Bình Dương |

        -   **Tiện ích**

            | Mã  | Công ty |
            |-----|-------------------------------------------------------------|
            | REE | Công ty Cổ phần Cơ Điện Lạnh REE |
            | PPC | Công ty Cổ phần Nhiệt điện Phả Lại |
            | NT2 | Công ty Cổ phần Điện lực Dầu khí Nhơn Trạch 2 |
            | POW | Tổng Công ty Điện lực Dầu khí Việt Nam |
            | PGV | Tổng Công ty Phát điện 3 |
            | CHP | Công ty Cổ phần Thủy điện Central Hydropower |
            | SJD | Công ty Cổ phần Thủy điện Cần Đơn |
            | TMP | Công ty Cổ phần Thủy điện Thác Mơ |

        -   **Viễn thông / CNTT**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | VGI | Công ty Cổ phần Đầu tư Quốc tế Viettel |
            | FPT | Công ty Cổ phần FPT |
            | CMG | Công ty Cổ phần Tập đoàn Công nghệ CMC |
            | FOX | Công ty Cổ phần Viễn thông FPT |
            | CTR | Công ty Cổ phần Công trình Viettel |
            | ABC | Công ty Cổ phần Truyền thông ABC |
            | VTC | Tổng Công ty Truyền thông Đa phương tiện VTC |

        -   **Phân phối & Bán lẻ**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | MWG | Công ty Cổ phần Đầu tư Thế Giới Di Động |
            | DGW | Công ty Cổ phần Thế Giới Số |
            | FRT | Công ty Cổ phần Bán lẻ Kỹ thuật số FPT |
            | PET | Tổng Công ty Cổ phần Dịch vụ Tổng hợp Dầu khí |
            | AST | Công ty Cổ phần Dịch vụ Hàng không Taseco |
            | BSR | Công ty Cổ phần Lọc hóa dầu Bình Sơn |
            | PIT | Công ty Cổ phần Xuất nhập khẩu Petrolimex |

        -   **Phần mềm**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | FPT | Công ty Cổ phần FPT |
            | CMG | Công ty Cổ phần Tập đoàn Công nghệ CMC |
            | CMC | Công ty Cổ phần Công nghệ CMC |
            | ITD | Công ty Cổ phần Công nghệ Tiên Phong |
            | SRA | Công ty Cổ phần Sara Việt Nam |
            | ELC | Công ty Cổ phần Điện tử - Tin học |
            | ADT | Công ty Cổ phần Viễn thông An Đạt |
            | ONE | Công ty Cổ phần Truyền thông ONE |

        -   **Dịch vụ tài chính (Chứng khoán)**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | SSI | Công ty Cổ phần Chứng khoán SSI |
            | HCM | Công ty Cổ phần Chứng khoán Thành phố Hồ Chí Minh |
            | VND | Công ty Cổ phần Chứng khoán VNDIRECT |
            | VCI | Công ty Cổ phần Chứng khoán Bản Việt |
            | BSI | Công ty Cổ phần Chứng khoán BIDV |
            | VIX | Công ty Cổ phần Chứng khoán VIX |
            | MBS | Công ty Cổ phần Chứng khoán MB |
            | CTS | Công ty Cổ phần Chứng khoán Công thương |

        -   **Năng lượng**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | GAS | Tổng Công ty Khí Việt Nam |
            | POW | Tổng Công ty Điện lực Dầu khí Việt Nam |
            | PLX | Công ty Cổ phần Tập đoàn Xăng dầu Việt Nam |
            | BSR | Công ty Cổ phần Lọc hóa dầu Bình Sơn |
            | PGD | Công ty Cổ phần Phân phối Khí thấp áp Dầu khí Việt Nam |
            | OIL | Tổng Công ty Dầu Việt Nam |
            | PC1 | Công ty Cổ phần Xây lắp điện 1 |
            | PVG | Công ty Cổ phần Kinh doanh LPG Việt Nam |

        -   **Hàng tiêu dùng**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | MSN | Công ty Cổ phần Tập đoàn Masan |
            | KDC | Công ty Cổ phần Thực phẩm Kinh Đô |
            | VNM | Công ty Cổ phần Sữa Việt Nam (Vinamilk) |
            | BHN | Tổng Công ty Cổ phần Bia Hà Nội |
            | QNS | Công ty Cổ phần Đường Quảng Ngãi |
            | PAN | Công ty Cổ phần Tập đoàn PAN |
            | LSS | Công ty Cổ phần Mía đường Lam Sơn |

        -   **Bảo hiểm**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | BVH | Tập đoàn Bảo Việt |
            | PVI | Công ty Cổ phần PVI |
            | MIG | Tổng Công ty Cổ phần Bảo hiểm Quân đội |
            | BMI | Tổng Công ty Cổ phần Bảo Minh |
            | BIC | Tổng Công ty Cổ phần Bảo hiểm BIDV |
            | PTI | Tổng Công ty Cổ phần Bảo hiểm Bưu điện |
            | ABI | Công ty Cổ phần Bảo hiểm Ngân hàng Nông nghiệp |
            | PRE | Công ty Cổ phần Tái bảo hiểm PVI |

        -   **Dịch vụ tiêu dùng / Trang sức**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | PNJ | Công ty Cổ phần Vàng bạc Đá quý Phú Nhuận |
            | HPG | Tập đoàn Hòa Phát |
            | MWG | Công ty Cổ phần Đầu tư Thế Giới Di Động |
            | SCS | Công ty Cổ phần Dịch vụ Hàng hóa Sài Gòn |
            | VJC | Công ty Cổ phần Hàng không Vietjet |
            | HVN | Tổng Công ty Hàng không Việt Nam |
            | AST | Công ty Cổ phần Dịch vụ Hàng không Taseco |

        -   **Dịch vụ thương mại**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | MWG | Công ty Cổ phần Đầu tư Thế Giới Di Động |
            | PNJ | Công ty Cổ phần Vàng bạc Đá quý Phú Nhuận |
            | VRE | Công ty Cổ phần Vincom Retail |
            | DGW | Công ty Cổ phần Thế Giới Số |
            | PET | Tổng Công ty Cổ phần Dịch vụ Tổng hợp Dầu khí |
            | PIT | Công ty Cổ phần Xuất nhập khẩu Petrolimex |
            | AMD | Công ty Cổ phần Đầu tư và Khoáng sản FLC Stone |

        -   **Ô tô & Linh kiện**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | HAX | Công ty Cổ phần Dịch vụ Ô tô Hàng Xanh |
            | TCH | Công ty Cổ phần Đầu tư Dịch vụ Tài chính Hoàng Huy |
            | TMT | Công ty Cổ phần Ô tô TMT |
            | DRC | Công ty Cổ phần Cao su Đà Nẵng |
            | SRC | Công ty Cổ phần Cao su Sao Vàng |
            | CSM | Công ty Cổ phần Công nghiệp Cao su Miền Nam |
            | HHS | Công ty Cổ phần Đầu tư Dịch vụ Hoàng Huy |
            | SVC | Công ty Cổ phần Dịch vụ Tổng hợp Sài Gòn |

        -   **Truyền thông & Giải trí**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | VGI | Công ty Cổ phần Đầu tư Quốc tế Viettel |
            | FPT | Công ty Cổ phần FPT |
            | CMG | Công ty Cổ phần Tập đoàn Công nghệ CMC |
            | VNG | Công ty Cổ phần VNG |
            | YEG | Công ty Cổ phần Tập đoàn Yeah1 |
            | EBS | Công ty Cổ phần Sách Giáo dục tại TP.HCM |
            | ADS | Công ty Cổ phần Damsan |
            | VTP | Công ty Cổ phần Viettel Post |

        -   **Dịch vụ chăm sóc sức khỏe**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | MED | Công ty Cổ phần Dược Mediplantex |
            | DHC | Công ty Cổ phần Đông Hải Bến Tre |
            | DBD | Công ty Cổ phần Dược - Vật tư Y tế Bình Định |
            | TNH | Công ty Cổ phần Bệnh viện Quốc tế Thái Nguyên |
            | VMD | Công ty Cổ phần Dược Vimedimex |
            | DVN | Tổng Công ty Dược Việt Nam |
            | FIT | Công ty Cổ phần Tập đoàn FIT |
            | JVC | Công ty Cổ phần Y tế Việt Nhật |

        -   **Đồ gia dụng**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | MWG | Công ty Cổ phần Đầu tư Thế Giới Di Động |
            | REE | Công ty Cổ phần Cơ Điện Lạnh REE |
            | GDT | Công ty Cổ phần Chế biến Gỗ Đức Thành |
            | RAL | Công ty Cổ phần Bóng đèn Phích nước Rạng Đông |
            | TLG | Công ty Cổ phần Tập đoàn Thiên Long |
            | PAC | Công ty Cổ phần Pin Ắc quy Miền Nam |
            | SHA | Công ty Cổ phần Sơn Hà Sài Gòn |

        -   **Phần cứng**

            | Mã | Công ty |
            |----|-------------------------------------------------------------|
            | FPT | Công ty Cổ phần FPT |
            | CMC | Công ty Cổ phần Công nghệ CMC |
            | CMG | Công ty Cổ phần Tập đoàn Công nghệ CMC |
            | GEX | Công ty Cổ phần Thiết bị điện Việt Nam |
            | DGW | Công ty Cổ phần Thế Giới Số |
            | VNZ | Công ty Cổ phần VNZ |
            | DNC | Công ty Cổ phần Điện nước lắp máy Hải Phòng |
            | ITD | Công ty Cổ phần Công nghệ Tiên Phong |

    -   **Mã chỉ số (Index) hay Chỉ số chứng khoán:** VN INDEX, VN30 INDEX, VN100 INDEX, HNX INDEX
        
    -   **Mã ETF (ETF Tickers) hay Mã quỹ ETF gồm các mã hỗ trợ:** E1VFVN30, FUEABVND, FUEBFVND, FUECMID, FUEFCV50, FUEIP100, FUEKIV30, FUEKIVFS, FUEKIVND, FUEMAV30, FUEMAVND, FUESSV30, FUESSV50, FUESSVFL, FUETC50, FUETPVND, FUEVFVND, FUEVN100
        
    -   **Mã Phái sinh (Derivatives) gồm Hợp đồng tương lai chỉ số (Index Futures) và Hợp đồng tương lai trái phiếu bao gồm:** VN30F*, GB05F*, GB10F*
        
-   **Các trường sẽ được lấy bao gồm:**
    
    | Trường   | Kiểu dữ liệu | Giải thích |
    |----------|--------------|-----------|
    | symbol   | str          | Mã chứng khoán hoặc mã giao dịch |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS | Thời điểm ghi nhận dữ liệu |
    | open     | float        | Giá mở cửa phiên giao dịch |
    | high     | float        | Giá cao nhất trong phiên |
    | low      | float        | Giá thấp nhất trong phiên |
    | close    | float        | Giá đóng cửa phiên giao dịch |
    | volume   | float        | Khối lượng giao dịch |
    

### 2) Trade Data

-   Dữ liệu giao dịch sẽ được lấy theo realtime cho các mã cổ phiếu, chỉ số, ETF và phái sinh đã liệt kê ở trên.
    
-   **Các trường sẽ được lấy bao gồm(riêng phái sinh sẽ có thêm trường mua bán):**
    
    | Trường   | Kiểu dữ liệu | Giải thích |
    |----------|--------------|-----------|
    | symbol   | str          | Mã chứng khoán hoặc mã giao dịch |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS | Thời điểm giao dịch |
    | volume   | float        | Khối lượng giao dịch |
    | price    | float        | Giá giao dịch |
    | change   | float        | Biến động giá so với phiên trước |
    | M/B      | str          | Loại giao dịch: Mua/Bán |


### 3) Orderbook Data

-   Dữ liệu giao dịch sẽ được lấy theo realtime cho các mã cổ phiếu, chỉ số, ETF và phái sinh đã liệt kê ở trên.


-   **Các trường sẽ được lấy bao gồm:**

    | Trường   | Kiểu dữ liệu | Giải thích |
    |----------|--------------|-----------|
    | symbol   | str          | Mã chứng khoán hoặc mã giao dịch |
    | bid_price| float        | Giá đặt mua |
    | bid_volume| float       | Khối lượng đặt mua |
    | ask_price| float        | Giá đặt bán |
    | ask_volume| float       | Khối lượng đặt bán |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS | Thời điểm ghi nhận dữ liệu |


### 4) Tỷ giá USD - VND tỉ giá bán (selling rate) từ 3 nguồn viettinbank , vietcombank , bidv

- Dữ liệu được lấy theo ngày nhưng update 5 phút 1 lần để lấy tỉ giá bán

    | Trường   | Kiểu dữ liệu | Giải thích |
    |----------|--------------|-----------|
    | symbol   | str          | Mã chứng khoán hoặc mã giao dịch |
    | bid_price| float        | Giá đặt mua |
    | bid_volume| float       | Khối lượng đặt mua |
    | ask_price| float        | Giá đặt bán |
    | ask_volume| float       | Khối lượng đặt bán |
    | datetime | datetime, cần format về YYYY-MM-DD HH:MM:SS | Thời điểm ghi nhận dữ liệu |
    | Trường        | Kiểu dữ liệu | Giải thích |
    |---------------|--------------|-----------|
    | datetime      | datetime, cần format về YYYY-MM-DD HH:MM:SS | Thời điểm ghi nhận dữ liệu |
    | selling_rate  | float        | Tỉ giá bán USD/VND |
    | cash          | float        | Tỉ giá tiền mặt |
    | transfer      | float        | Tỉ giá chuyển khoản |

## B. DỮ LIỆU CRYPTO

### 1) Trade
*Dữ liệu các giao dịch khớp lệnh trên sàn, ghi lại từng lần mua/bán thực tế.*
| Trường | Kiểu dữ liệu |
| Trường     | Kiểu dữ liệu | Giải thích |
|------------|--------------|-----------|
| symbol     | varchar      | Mã đồng coin hoặc cặp giao dịch |
| price      | float        | Giá giao dịch |
| trade_time | datetime     | Thời điểm giao dịch |
| quantity   | float        | Khối lượng giao dịch |
| maker      | bool         | Maker (người tạo lệnh) |

### 2) Depth
*Dữ liệu sổ lệnh (Orderbook), thể hiện các mức giá và khối lượng đặt mua/bán tại từng thời điểm.*
| Trường | Kiểu dữ liệu |
| Trường        | Kiểu dữ liệu | Giải thích |
|---------------|--------------|-----------|
| symbol        | varchar      | Mã đồng coin hoặc cặp giao dịch |
| side          | varchar      | Loại lệnh: mua/bán |
| price         | decimal      | Giá đặt lệnh |
| quantity      | decimal      | Khối lượng đặt lệnh |
| amount_total  | decimal      | Tổng giá trị lệnh |
| updated_at    | timestamp    | Thời điểm cập nhật |

### 3) CoinMarketCapData
*Dữ liệu tổng hợp từ CoinMarketCap, gồm giá, vốn hóa, khối lượng, thứ hạng và các chỉ số biến động của đồng coin.*
| Trường | Kiểu dữ liệu |
| Trường              | Kiểu dữ liệu | Giải thích |
|---------------------|--------------|-----------|
| symbol              | varchar      | Mã đồng coin |
| name                | varchar      | Tên đồng coin |
| datetime            | datetime     | Thời điểm ghi nhận dữ liệu |
| price               | float        | Giá hiện tại |
| cmc_rank            | int          | Thứ hạng trên CoinMarketCap |
| change_1h_percent   | float        | % thay đổi giá trong 1 giờ |
| change_24h_percent  | float        | % thay đổi giá trong 24 giờ |
| change_7d_percent   | float        | % thay đổi giá trong 7 ngày |
| volume              | float        | Khối lượng giao dịch |
| market_cap          | float        | Vốn hóa thị trường |
| volume_24h          | float        | Khối lượng giao dịch 24h |
| circulating_supply  | float        | Lượng cung lưu thông |

### 4) Dominance
*Dữ liệu thể hiện tỷ trọng (dominance) của một đồng coin so với toàn thị trường, gồm giá mở, cao, thấp, đóng và khối lượng.*
| Trường | Kiểu dữ liệu |
| Trường   | Kiểu dữ liệu | Giải thích |
|----------|--------------|-----------|
| symbol   | varchar      | Mã đồng coin |
| open     | float        | Giá mở cửa |
| high     | float        | Giá cao nhất |
| low      | float        | Giá thấp nhất |
| close    | float        | Giá đóng cửa |
| volume   | float        | Khối lượng giao dịch |
| type     | varchar      | Loại dữ liệu dominance |
| datetime | datetime     | Thời điểm ghi nhận dữ liệu |

### 5) funding_rate
*Dữ liệu funding rate (lãi suất qua đêm) của các hợp đồng phái sinh, gồm giá, thời gian, loại hợp đồng và các chỉ số liên quan.*
| Trường | Kiểu dữ liệu |
| Trường            | Kiểu dữ liệu | Giải thích |
|-------------------|--------------|-----------|
| symbol            | varchar      | Mã đồng coin |
| funding_rate      | decimal      | Lãi suất qua đêm |
| funding_time      | timestamp    | Thời điểm tính funding rate |
| mark_price        | decimal      | Giá mark (tham chiếu) |
| index_price       | decimal      | Giá index (chỉ số) |
| type              | varchar      | Loại hợp đồng |
| next_funding_time | timestamp    | Thời điểm funding tiếp theo |

### 6) Kline
*Dữ liệu nến (Kline/Candlestick), gồm giá mở, cao, thấp, đóng, khối lượng và thời gian cho từng khung thời gian.*
| Trường | Kiểu dữ liệu |
| Trường     | Kiểu dữ liệu | Giải thích |
|------------|--------------|-----------|
| symbol     | varchar      | Mã đồng coin |
| interval   | varchar      | Khung thời gian nến |
| open_time  | timestamp    | Thời điểm mở nến |
| open       | decimal      | Giá mở cửa |
| high       | decimal      | Giá cao nhất |
| low        | decimal      | Giá thấp nhất |
| close      | decimal      | Giá đóng cửa |
| volume     | decimal      | Khối lượng giao dịch |
| close_time | timestamp    | Thời điểm đóng nến |

### 7) Liquidation
*Dữ liệu các lệnh thanh lý (liquidation) trên thị trường phái sinh, gồm giá, khối lượng, chiều lệnh và thời gian.*
| Trường | Kiểu dữ liệu |
| Trường   | Kiểu dữ liệu | Giải thích |
|----------|--------------|-----------|
| symbol   | varchar      | Mã đồng coin |
| price    | decimal      | Giá thanh lý |
| quantity | decimal      | Khối lượng thanh lý |
| side     | varchar      | Chiều lệnh: mua/bán |
| time     | timestamp    | Thời điểm thanh lý |

### 8) exchange_info
*Thông tin về sàn giao dịch, múi giờ và thời điểm cập nhật.*
| Trường | Kiểu dữ liệu |
| Trường        | Kiểu dữ liệu | Giải thích |
|---------------|--------------|-----------|
| exchange_name | varchar      | Tên sàn giao dịch |
| timezone      | varchar      | Múi giờ sàn giao dịch |
| datetime      | timestamp    | Thời điểm cập nhật |

### 9) open_interest
*Dữ liệu open interest (khối lượng hợp đồng mở) của các hợp đồng phái sinh tại từng thời điểm.*
| Trường | Kiểu dữ liệu |
| Trường        | Kiểu dữ liệu | Giải thích |
|---------------|--------------|-----------|
| symbol        | varchar      | Mã đồng coin hoặc hợp đồng |
| open_interest | decimal      | Khối lượng hợp đồng mở |
| timestamp     | timestamp    | Thời điểm ghi nhận dữ liệu |