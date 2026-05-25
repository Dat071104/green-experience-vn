from app import create_app

# ⭐ QUAN TRỌNG: app PHẢI được tạo ở module level, không trong if block
app = create_app('production')

if __name__ == '__main__':
    app.run(debug=False)