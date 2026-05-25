DESTINATIONS = [
    {
        'id': 'lo-lo-chai',
        'name': 'Lô Lô Chải, Hà Giang',
        'region': 'Miền Bắc',
        'image': 'https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&q=80',
        'description': 'Làng văn hóa Lô Lô Chải nằm ngay dưới chân cột cờ Lũng Cú. Trải nghiệm không gian sống truyền thống với nhà trình tường bằng đất, mái ngói âm dương và những phong tục đậm đà bản sắc người Lô Lô.',
        'highlights': ['Nhà trình tường truyền thống', 'Văn hóa người Lô Lô', 'Cột cờ Lũng Cú', 'Cà phê Cực Bắc']
    },
    {
        'id': 'mang-den',
        'name': 'Măng Đen, Kon Tum',
        'region': 'Tây Nguyên',
        'image': 'https://images.unsplash.com/photo-1598436814911-37d363b963a7?auto=format&fit=crop&q=80',
        'description': 'Được mệnh danh là "Đà Lạt thứ hai" với rừng thông bạt ngàn, không khí mát mẻ quanh năm. Du lịch Măng Đen gắn liền với bảo tồn thiên nhiên và hỗ trợ cộng đồng dân tộc bản địa.',
        'highlights': ['Rừng thông nguyên sinh', 'Thác Pa Sỹ', 'Làng văn hóa Kon Pring', 'Nông trại sinh thái']
    },
    {
        'id': 'tien-giang',
        'name': 'Tiền Giang - Bến Tre',
        'region': 'Miền Tây',
        'image': 'https://images.unsplash.com/photo-1604928169976-5832049e6123?auto=format&fit=crop&q=80',
        'description': 'Hành trình xanh về miền Tây sông nước. Tham gia các hoạt động du lịch có trách nhiệm, chèo xuồng ba lá dưới tán dừa nước, và trải nghiệm cuộc sống người dân đồng bằng sông Cửu Long.',
        'highlights': ['Vườn trái cây sinh thái', 'Chèo xuồng ba lá', 'Làng nghề truyền thống', 'Đờn ca tài tử']
    },
    {
        'id': 'pu-luong',
        'name': 'Pù Luông, Thanh Hóa',
        'region': 'Miền Bắc',
        'image': 'https://images.unsplash.com/photo-1579450841285-1d033758b991?auto=format&fit=crop&q=80',
        'description': 'Khu bảo tồn thiên nhiên Pù Luông nổi tiếng với những thửa ruộng bậc thang tuyệt đẹp, hệ sinh thái đa dạng và những bản làng người Thái, người Mường bình yên.',
        'highlights': ['Ruộng bậc thang Bản Hiêu', 'Bản Đôn', 'Chèo bè tre', 'Trekking xuyên rừng']
    },
    {
        'id': 'phong-nha',
        'name': 'Phong Nha, Quảng Bình',
        'region': 'Miền Trung',
        'image': 'https://images.unsplash.com/photo-1563293816-17b5f54314c4?auto=format&fit=crop&q=80',
        'description': 'Vương quốc hang động thế giới với Vườn quốc gia Phong Nha - Kẻ Bàng. Các hoạt động du lịch ở đây chú trọng bảo tồn thiên nhiên, giảm thiểu tác động đến môi trường hang động.',
        'highlights': ['Động Phong Nha', 'Suối Nước Moọc', 'Tour bảo tồn động vật hoang dã', 'Rừng nguyên sinh']
    },
    {
        'id': 'cat-ba',
        'name': 'Cát Bà, Hải Phòng',
        'region': 'Miền Bắc',
        'image': 'https://images.unsplash.com/photo-1627916972049-340915a133f9?auto=format&fit=crop&q=80',
        'description': 'Khu dự trữ sinh quyển thế giới Cát Bà mang đến trải nghiệm du lịch xanh giữa biển đảo. Tham gia dọn rác bãi biển, trồng rừng ngập mặn và bảo tồn voọc Cát Bà.',
        'highlights': ['Vườn quốc gia Cát Bà', 'Vịnh Lan Hạ', 'Làng chài Việt Hải', 'Chèo Kayak nhặt rác']
    }
]

TOURS = [
    {
        'id': 'tour-lo-lo-chai-1',
        'title': 'Hành Trình Văn Hóa Lô Lô Chải',
        'destinationId': 'lo-lo-chai',
        'duration': '3 Ngày 2 Đêm',
        'price': 3500000,
        'image': 'https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&q=80',
        'greenPoints': 300,
        'co2Saved': 45.5,
        'description': 'Trải nghiệm cuộc sống người Lô Lô, học làm đồ thủ công truyền thống và tham gia dọn dẹp môi trường làng bản.',
        'itinerary': [
            {'day': 1, 'content': 'Hà Giang - Lũng Cú. Nhận phòng homestay Lô Lô, giao lưu văn hóa.'},
            {'day': 2, 'content': 'Tham gia dọn dẹp đường làng, học thêu thổ cẩm cùng phụ nữ bản.'},
            {'day': 3, 'content': 'Thăm Cột Cờ Lũng Cú, trekking nhẹ nhàng và trở về Hà Giang.'}
        ],
        'included': ['Homestay bản địa', 'Ăn uống thực phẩm địa phương', 'Hướng dẫn viên bản địa', 'Vật dụng bảo vệ môi trường'],
        'notIncluded': ['Vé máy bay', 'Chi tiêu cá nhân'],
        'greenActivities': ['Dọn rác đường làng', 'Sử dụng bình nước cá nhân', 'Không túi nilon']
    },
    {
        'id': 'tour-mang-den-1',
        'title': 'Măng Đen - Trồng Rừng & Tình Nguyện',
        'destinationId': 'mang-den',
        'duration': '4 Ngày 3 Đêm',
        'price': 4200000,
        'image': 'https://images.unsplash.com/photo-1598436814911-37d363b963a7?auto=format&fit=crop&q=80',
        'greenPoints': 400,
        'co2Saved': 80.0,
        'description': 'Khám phá thiên nhiên Măng Đen, tham gia dự án trồng thông và giao lưu với trẻ em làng Kon Pring.',
        'itinerary': [
            {'day': 1, 'content': 'Đến Măng Đen, thăm thác Pa Sỹ, nhận phòng homestay sinh thái.'},
            {'day': 2, 'content': 'Tham gia dự án trồng thông tại rừng phòng hộ Măng Đen.'},
            {'day': 3, 'content': 'Giao lưu cộng đồng làng Kon Pring, dạy học hoặc chơi cùng trẻ em.'},
            {'day': 4, 'content': 'Thăm hồ Đăk Ke, tổng kết hành trình xanh.'}
        ],
        'included': ['Cây giống trồng rừng', 'Lưu trú sinh thái', 'Di chuyển xe chung', 'Bảo hiểm'],
        'notIncluded': ['Vé máy bay/xe khách đến Kon Tum'],
        'greenActivities': ['Trồng cây xanh', 'Ăn chay 1 bữa', 'Di chuyển xe đạp']
    },
    {
        'id': 'tour-tien-giang-1',
        'title': 'Miền Tây Zero Waste Tour',
        'destinationId': 'tien-giang',
        'duration': '2 Ngày 1 Đêm',
        'price': 1800000,
        'image': 'https://images.unsplash.com/photo-1604928169976-5832049e6123?auto=format&fit=crop&q=80',
        'greenPoints': 200,
        'co2Saved': 25.0,
        'description': 'Du lịch miền Tây không rác thải nhựa, kết hợp trồng bần giữ đất và đạp xe dạo quanh miệt vườn.',
        'itinerary': [
            {'day': 1, 'content': 'Sài Gòn - Tiền Giang. Đạp xe quanh cồn, tham quan vườn trái cây sạch.'},
            {'day': 2, 'content': 'Chèo ghe vớt rác trên kênh, trồng bần chống sạt lở ven sông.'}
        ],
        'included': ['Homestay miệt vườn', 'Ăn uống đặc sản', 'Xe đạp', 'Dụng cụ vớt rác'],
        'notIncluded': ['Chi tiêu cá nhân'],
        'greenActivities': ['Vớt rác trên sông', 'Zero-waste', 'Di chuyển xe đạp']
    },
    {
        'id': 'tour-pu-luong-1',
        'title': 'Pù Luông Trekking Sinh Thái',
        'destinationId': 'pu-luong',
        'duration': '3 Ngày 2 Đêm',
        'price': 2900000,
        'image': 'https://images.unsplash.com/photo-1579450841285-1d033758b991?auto=format&fit=crop&q=80',
        'greenPoints': 350,
        'co2Saved': 50.0,
        'description': 'Trekking qua các bản làng, nghỉ tại nhà sàn truyền thống và hỗ trợ người dân cải tạo hệ thống tưới tiêu.',
        'itinerary': [
            {'day': 1, 'content': 'Hà Nội - Pù Luông. Trekking từ Bản Đôn, nhận phòng nhà sàn.'},
            {'day': 2, 'content': 'Trekking Bản Hiêu, hỗ trợ dân làng dọn dẹp kênh mương thủy lợi.'},
            {'day': 3, 'content': 'Thăm chợ phiên, mua nông sản ủng hộ địa phương và trở về.'}
        ],
        'included': ['Lưu trú nhà sàn', 'Ăn uống bản địa', 'HDV địa phương'],
        'notIncluded': ['Tiền tip'],
        'greenActivities': ['Trekking', 'Hỗ trợ nông nghiệp', 'Mua nông sản bản địa']
    },
    {
        'id': 'tour-phong-nha-1',
        'title': 'Phong Nha - Khám Phá Rừng & Hang Động Xanh',
        'destinationId': 'phong-nha',
        'duration': '3 Ngày 2 Đêm',
        'price': 4500000,
        'image': 'https://images.unsplash.com/photo-1563293816-17b5f54314c4?auto=format&fit=crop&q=80',
        'greenPoints': 350,
        'co2Saved': 40.0,
        'description': 'Khám phá vẻ đẹp Phong Nha kết hợp tìm hiểu công tác cứu hộ động vật hoang dã tại Vườn Quốc Gia.',
        'itinerary': [
            {'day': 1, 'content': 'Tham quan Động Phong Nha bằng xuồng máy thân thiện môi trường.'},
            {'day': 2, 'content': 'Eco-tour bảo tồn: tìm hiểu trung tâm cứu hộ động vật hoang dã.'},
            {'day': 3, 'content': 'Chèo kayak tại Suối Nước Moọc, cam kết không sử dụng nhựa.'}
        ],
        'included': ['Homestay thân thiện', 'Vé tham quan', 'Đóng góp quỹ bảo tồn'],
        'notIncluded': ['Chi phí di chuyển đến Phong Nha'],
        'greenActivities': ['Không rác nhựa', 'Hỗ trợ quỹ bảo tồn động vật', 'Di chuyển chèo thuyền']
    },
    {
        'id': 'tour-cat-ba-1',
        'title': 'Cát Bà - Chiến Dịch Biển Sạch',
        'destinationId': 'cat-ba',
        'duration': '2 Ngày 1 Đêm',
        'price': 2100000,
        'image': 'https://images.unsplash.com/photo-1627916972049-340915a133f9?auto=format&fit=crop&q=80',
        'greenPoints': 250,
        'co2Saved': 30.0,
        'description': 'Kết hợp nghỉ dưỡng tại vịnh Lan Hạ và tham gia hoạt động chèo kayak dọn rác bảo vệ môi trường biển.',
        'itinerary': [
            {'day': 1, 'content': 'Hà Nội - Cát Bà. Nhận phòng homestay sinh thái, thăm làng Việt Hải.'},
            {'day': 2, 'content': 'Chèo Kayak vịnh Lan Hạ kết hợp dọn rác trên mặt biển và vách đá.'}
        ],
        'included': ['Lưu trú sinh thái', 'Thuyền kayak', 'Dụng cụ nhặt rác', 'Ăn uống hải sản bền vững'],
        'notIncluded': ['Chi tiêu cá nhân'],
        'greenActivities': ['Dọn rác biển', 'Di chuyển bằng xe đạp tại làng Việt Hải', 'Bảo tồn Voọc']
    }
]

HOMESTAYS = [
    {
        'id': 'hs-lolo-1',
        'name': 'Lolo Village Homestay',
        'destinationId': 'lo-lo-chai',
        'image': 'https://images.unsplash.com/photo-1621508654686-809f23efdabc?auto=format&fit=crop&q=80',
        'greenScore': 90,
        'features': ['Nhà trình tường', 'Năng lượng mặt trời', 'Không nhựa dùng 1 lần', 'Thực phẩm hữu cơ']
    },
    {
        'id': 'hs-mangden-1',
        'name': 'Bạch Dương Eco-Homestay',
        'destinationId': 'mang-den',
        'image': 'https://images.unsplash.com/photo-1542718610-a1d656d1884c?auto=format&fit=crop&q=80',
        'greenScore': 85,
        'features': ['Gỗ tái chế', 'Trồng rau sạch', 'Thu gom nước mưa']
    },
    {
        'id': 'hs-tiengiang-1',
        'name': 'Mekong Rustic',
        'destinationId': 'tien-giang',
        'image': 'https://images.unsplash.com/photo-1596423735880-5fec6d46dc72?auto=format&fit=crop&q=80',
        'greenScore': 95,
        'features': ['Kiến trúc lá dừa', 'Ủ phân hữu cơ', 'Sản phẩm tẩy rửa sinh học', 'Zero Waste']
    },
    {
        'id': 'hs-puluong-1',
        'name': 'Pù Luông Eco Garden',
        'destinationId': 'pu-luong',
        'image': 'https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&q=80',
        'greenScore': 88,
        'features': ['Nhà sàn truyền thống', 'Vật liệu tự nhiên', 'Không rác nhựa', 'Hỗ trợ cộng đồng']
    },
    {
        'id': 'hs-phongnha-1',
        'name': 'Phong Nha Farmstay',
        'destinationId': 'phong-nha',
        'image': 'https://images.unsplash.com/photo-1444201983204-c43cbd584d93?auto=format&fit=crop&q=80',
        'greenScore': 92,
        'features': ['Năng lượng mặt trời', 'Nông nghiệp sạch', 'Bể bơi tự nhiên']
    }
]

PLASTIC_FREE_SPOTS = [
    {
        'id': 'pf-lolo-1',
        'name': 'Cà Phê Cực Bắc',
        'type': 'Quán Cafe',
        'destinationId': 'lo-lo-chai',
        'description': 'Sử dụng ly sứ và ống hút tre 100%'
    },
    {
        'id': 'pf-mangden-1',
        'name': 'Măng Đen Chay',
        'type': 'Nhà Hàng',
        'destinationId': 'mang-den',
        'description': 'Nhà hàng chay sử dụng khay gỗ, mẹt tre, không túi nilon'
    },
    {
        'id': 'pf-tiengiang-1',
        'name': 'Chợ Quê Sinh Thái Cồn Thới Sơn',
        'type': 'Khu Chợ',
        'destinationId': 'tien-giang',
        'description': 'Gói hàng bằng lá chuối, khuyến khích mang làn/giỏ đi chợ'
    },
    {
        'id': 'pf-phongnha-1',
        'name': 'Eco Station',
        'type': 'Quán Cafe & Refill',
        'destinationId': 'phong-nha',
        'description': 'Trạm làm đầy nước miễn phí, bán đồ dùng thân thiện môi trường'
    }
]

COMMUNITY_ACTIVITIES = [
    {
        'id': 'act-1',
        'title': 'Dọn Rác Bản Làng',
        'destinationId': 'lo-lo-chai',
        'type': 'Môi trường',
        'duration': '2 giờ',
        'gp_reward': 50,
        'impact': '10kg rác thu gom'
    },
    {
        'id': 'act-2',
        'title': 'Trồng Rừng Thông',
        'destinationId': 'mang-den',
        'type': 'Môi trường',
        'duration': '3 giờ',
        'gp_reward': 100,
        'impact': '5 cây thông được trồng'
    },
    {
        'id': 'act-3',
        'title': 'Dạy Tiếng Anh Trẻ Em',
        'destinationId': 'mang-den',
        'type': 'Giáo dục',
        'duration': '2 giờ',
        'gp_reward': 80,
        'impact': '15 trẻ em tham gia'
    },
    {
        'id': 'act-4',
        'title': 'Trồng Cây Bần Chống Sạt Lở',
        'destinationId': 'tien-giang',
        'type': 'Môi trường',
        'duration': '4 giờ',
        'gp_reward': 120,
        'impact': '20 cây bần được trồng'
    },
    {
        'id': 'act-5',
        'title': 'Làm Kênh Mương Thủy Lợi',
        'destinationId': 'pu-luong',
        'type': 'Cộng đồng',
        'duration': '3 giờ',
        'gp_reward': 90,
        'impact': 'Hỗ trợ 5 hộ nông dân'
    },
    {
        'id': 'act-6',
        'title': 'Cứu Hộ Động Vật Hoang Dã',
        'destinationId': 'phong-nha',
        'type': 'Bảo tồn',
        'duration': 'Nửa ngày',
        'gp_reward': 150,
        'impact': 'Đóng góp 200,000VNĐ vào quỹ'
    }
]

GREEN_POINTS_REWARDS = [
    {'id': 'rwd-1', 'title': 'Voucher Giảm 50% Homestay', 'cost': 500, 'type': 'voucher'},
    {'id': 'rwd-2', 'title': 'Bộ Ống Hút Tre Tự Nhiên', 'cost': 150, 'type': 'merch'},
    {'id': 'rwd-3', 'title': 'Bình Nước Giữ Nhiệt Lõi Inox', 'cost': 300, 'type': 'merch'},
    {'id': 'rwd-4', 'title': 'Góp 1 Cây Xanh Quỹ Trồng Rừng', 'cost': 200, 'type': 'donation'},
    {'id': 'rwd-5', 'title': 'Voucher Tour Giảm 10%', 'cost': 800, 'type': 'voucher'},
    {'id': 'rwd-6', 'title': 'Túi Tote Sinh Thái Tái Chế', 'cost': 250, 'type': 'merch'}
]

# Helper lookups
DESTINATIONS_BY_ID = {d['id']: d for d in DESTINATIONS}
TOURS_BY_ID = {t['id']: t for t in TOURS}
TOURS_BY_DESTINATION = {}
for t in TOURS:
    TOURS_BY_DESTINATION.setdefault(t['destinationId'], []).append(t)
