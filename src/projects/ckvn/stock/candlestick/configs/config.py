import os
from dotenv import load_dotenv

load_dotenv()


SYMBOL = {
    "ngan_hang": {
        "VCB": "Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank)",
        "BID": "Ngân hàng TMCP Đầu tư và Phát triển Việt Nam (BIDV)",
        "CTG": "Ngân hàng TMCP Công thương Việt Nam (VietinBank)",
        "TPB": "Ngân hàng TMCP Tiên Phong (TPBank)",
        "MBB": "Ngân hàng Quân đội (MB Bank)",
        "ACB": "Ngân hàng Á Châu",
        "SHB": "Ngân hàng TMCP Sài Gòn - Hà Nội",
        "VPB": "Ngân hàng TMCP Việt Nam Thịnh Vượng",
        "TCB": "Ngân hàng TMCP Kỹ thương Việt Nam",
    },
    "bat_dong_san": {
        "VHM": "Vinhomes",
        "NVL": "Novaland",
        "HDG": "Tập đoàn Hà Đô",
        "DXG": "Đất Xanh Group",
        "KDH": "Địa ốc Khang Điền",
        "BCM": "Tập đoàn Becamex IDC",
        "PDR": "Phát triển Bất động sản Phát Đạt",
    },
    "thep_cong_nghiep": {
        "HPG": "Tập đoàn Hòa Phát",
        "NKG": "Thép Nam Kim",
        "HSG": "Tập đoàn Hoa Sen",
        "VIC": "Tập đoàn Vingroup",
        "DHC": "Công ty Cổ phần Đông Hải Bến Tre",
    },
    "tieu_dung_thuc_pham": {
        "VNM": "Công ty Cổ phần Sữa Việt Nam (Vinamilk)",
        "MWG": "Công ty Cổ phần Đầu tư Thế Giới Di Động",
        "PNJ": "Công ty Cổ phần Vàng bạc Đá quý Phú Nhuận",
        "MSN": "Tập đoàn Masan",
        "SAB": "Sabeco",
        "KDC": "Công ty Cổ phần Thực phẩm Kinh Đô",
        "BHN": "Bia Hà Nội",
        "QNS": "Đường Quảng Ngãi",
        "SBT": "Thành Thành Công - Biên Hòa",
        "PAN": "Tập đoàn PAN",
        "VCF": "Vinacafe Biên Hòa",
    },
    "cong_nghe_vien_thong": {
        "FPT": "Công ty Cổ phần FPT",
        "VGI": "Công ty Cổ phần Đầu tư Quốc tế Viettel",
        "VTP": "Công ty Cổ phần Viettel Post",
        "CMG": "Tập đoàn Công nghệ CMC",
        "CMC": "Công ty Cổ phần Công nghệ CMC",
        "FOX": "Công ty Cổ phần Viễn thông FPT",
        "CTR": "Công ty Cổ phần Công trình Viettel",
        "VTC": "Tổng Công ty Truyền thông Đa phương tiện VTC",
    },
    "nang_luong": {
        "GAS": "Tổng Công ty Khí Việt Nam",
        "POW": "Tổng Công ty Điện lực Dầu khí Việt Nam",
        "PLX": "Tập đoàn Xăng dầu Việt Nam",
        "BSR": "Công ty Cổ phần Lọc hóa dầu Bình Sơn",
        "PGD": "Công ty Cổ phần Phân phối Khí thấp áp Dầu khí Việt Nam",
        "OIL": "Tổng Công ty Dầu Việt Nam",
        "PC1": "Công ty Cổ phần Xây lắp điện 1",
        "PVG": "Công ty Cổ phần Kinh doanh LPG Việt Nam",
    },
    "chung_khoan": {
        "SSI": "Công ty Cổ phần Chứng khoán SSI",
        "HCM": "Công ty Cổ phần Chứng khoán TP.HCM",
        "VND": "Công ty Cổ phần Chứng khoán VNDIRECT",
        "VCI": "Công ty Cổ phần Chứng khoán Bản Việt",
        "BSI": "Công ty Cổ phần Chứng khoán BIDV",
        "VIX": "Công ty Cổ phần Chứng khoán VIX",
        "MBS": "Công ty Cổ phần Chứng khoán MB",
        "CTS": "Công ty Cổ phần Chứng khoán Công thương",
    },
    "bao_hiem": {
        "BVH": "Tập đoàn Bảo Việt",
        "PVI": "Công ty Cổ phần PVI",
        "MIG": "Tổng Công ty Cổ phần Bảo hiểm Quân đội",
        "BMI": "Tổng Công ty Cổ phần Bảo Minh",
        "BIC": "Tổng Công ty Cổ phần Bảo hiểm BIDV",
        "PTI": "Tổng Công ty Cổ phần Bảo hiểm Bưu điện",
        "ABI": "Công ty Cổ phần Bảo hiểm Ngân hàng Nông nghiệp",
        "PRE": "Công ty Cổ phần Tái bảo hiểm PVI",
    },
}

ACTIVE_TIMES = {
    "morning": "09:00:00-11:30:00",
    "afternoon": "13:00:00-14:45:00",
}

SYMBOL_API = {
    "investing_api": os.getenv("INVESTING_API"),
    "vps_api": os.getenv("VPS_API"),
}
