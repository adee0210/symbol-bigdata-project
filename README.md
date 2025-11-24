# I. DATA SOURCE

## A. DỮ LIỆU CHỨNG KHOÁN VIỆT NAM

**Thời gian giao dịch cổ phiếu, ETF (HOSE, HNX, UPCoM):**

Phiên

Thời gian

Ghi chú

Khớp lệnh định kỳ mở cửa (ATO)

9:00 – 9:15

Xác định giá mở cửa

Khớp lệnh liên tục

9:15 – 11:30

Giao dịch theo giá thỏa thuận giữa mua và bán

Nghỉ trưa

11:30 – 13:00

Không giao dịch

Khớp lệnh liên tục buổi chiều

13:00 – 14:30 (HOSE), 13:00 – 15:00 (HNX/UPCoM)

Giao dịch bình thường

Khớp lệnh định kỳ đóng cửa (ATC)

14:30 – 14:45 (HOSE), 15:00 – 15:05 (HNX/UPCoM)

Xác định giá đóng cửa

**Lưu ý:**

-   **ATO (At The Open)**: Giá mở cửa, lệnh được khớp theo giá xác định.
-   **ATC (At The Close)**: Giá đóng cửa, lệnh được khớp theo giá xác định.
-   **Khớp lệnh liên tục**: Giá thay đổi theo cung-cầu từng phút.

**Thời gian giao dịch phái sinh (Index Futures VN30):**

-   **Sáng**: 9:00 – 11:30
-   **Chiều**: 13:00 – 15:00

### 1) Candlestick Data

-   Các data source sẽ được lấy theo timeframe là theo 1 phút (1m) sẽ được crawl theo lịch sử và realtime bao gồm:
    
    -   **Mã cổ phiếu (Stocks) hay Cổ phiếu gồm:**
        
        -   **Ngân hàng**
            
            Mã
            
            Công ty
            
            VCB
            
            Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank)
            
            BID
            
            Ngân hàng TMCP Đầu tư và Phát triển Việt Nam (BIDV)
            
            CTG
            
            Ngân hàng TMCP Công thương Việt Nam (VietinBank)
            
            TPB
            
            Ngân hàng TMCP Tiên Phong (TPBank)
            
            MBB
            
            Ngân hàng Quân đội (MB Bank)
            
            ACB
            
            Ngân hàng Á Châu
            
            SHB
            
            Ngân hàng TMCP Sài Gòn - Hà Nội
            
            VPB
            
            Ngân hàng TMCP Việt Nam Thịnh Vượng
            
            TCB
            
            Ngân hàng TMCP Kỹ thương Việt Nam
            
        -   **Bất động sản**
            
            Mã
            
            Công ty
            
            VHM
            
            Vinhomes
            
            NVL
            
            Novaland
            
            HDG
            
            Tập đoàn Hà Đô
            
            DXG
            
            Đất Xanh Group
            
            KDH
            
            Địa ốc Khang Điền
            
            BCM
            
            Tập đoàn Becamex IDC
            
            PDR
            
            Phát triển Bất động sản Phát Đạt
            
        -   **Công nghiệp & Thép**
            
            Mã
            
            Công ty
            
            HPG
            
            Tập đoàn Hòa Phát
            
            NKG
            
            Thép Nam Kim
            
            HSG
            
            Tôn Hoa Sen
            
            VIC
            
            Tập đoàn Vingroup (công nghiệp, bất động sản, bán lẻ)
            
            DHC
            
            Công ty Cổ phần Đông Hải Bến Tre
            
        -   **Tiêu dùng & Thực phẩm**
            
            Mã
            
            Công ty
            
            VNM
            
            Vinamilk
            
            MWG
            
            Thế Giới Di Động
            
            PNJ
            
            Vàng bạc PNJ
            
            MSN
            
            Tập đoàn Masan
            
            SAB
            
            Sabeco
            
        -   **Dịch vụ & Viễn thông**
            
            Mã
            
            Công ty
            
            FPT
            
            FPT Corporation
            
            VGI
            
            VGI Holdings (Quảng cáo, logistics)
            
            VTP
            
            Viettel Post (trên UPCoM)
            
            GAS
            
            PV Gas
            
            VJC
            
            Vietjet Air
            
            HVN
            
            Vietnam Airlines
            
    -   **Mã chỉ số (Index) hay Chỉ số chứng khoán:** VN INDEX, VN30 INDEX, VN100 INDEX, HNX INDEX
        
    -   **Mã ETF (ETF Tickers) hay Mã quỹ ETF gồm các mã hỗ trợ:** E1VFVN30, FUEABVND, FUEBFVND, FUECMID, FUEFCV50, FUEIP100, FUEKIV30, FUEKIVFS, FUEKIVND, FUEMAV30, FUEMAVND, FUESSV30, FUESSV50, FUESSVFL, FUETC50, FUETPVND, FUEVFVND, FUEVN100
        
    -   **Mã Phái sinh (Derivatives) gồm Hợp đồng tương lai chỉ số (Index Futures) và Hợp đồng tương lai trái phiếu bao gồm:** VN30F*, GB05F*, GB10F*
        
-   **Các trường sẽ được lấy bao gồm:**
    
    Trường
    
    Kiểu dữ liệu
    
    symbol
    
    str
    
    datetime
    
    datetime, cần format về YYYY-MM-DD HH:MM:SS
    
    open
    
    float
    
    high
    
    float
    
    low
    
    float
    
    close
    
    float
    
    volume
    
    float
    

### 2) Trade Data

-   Dữ liệu giao dịch sẽ được lấy theo realtime cho các mã cổ phiếu, chỉ số, ETF và phái sinh đã liệt kê ở trên.
    
-   **Các trường sẽ được lấy bao gồm(riêng phái sinh sẽ có thêm trường mua bán):**
    
    Trường
    
    Kiểu dữ liệu
    
    symbol
    
    str
    
    datetime
    
    datetime, cần format về YYYY-MM-DD HH:MM:SS
    
    volume
    
    float
    
    price
    
    float
    
    change
    
    float
    
    M/B
    
    str