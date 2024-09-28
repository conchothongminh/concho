import streamlit as st
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title('Biểu đồ Giá kim cương theo Carat')

# Ví dụ về dữ liệu giá kim cương và carat (giả định)
carat = [0.2, 0.5, 1.0, 1.5, 2.0, 3.0]
price = [500, 1500, 5000, 10000, 20000, 40000]

# Tạo biểu đồ phân tán (scatter plot)
fig, ax = plt.subplots()
ax.scatter(carat, price, color='blue')

# Thêm tiêu đề và nhãn trục
ax.set_title('Giá kim cương theo carat')
ax.set_xlabel('Carat')
ax.set_ylabel('Giá (USD)')

# Hiển thị biểu đồ trên ứng dụng Streamlit
st.pyplot(fig)
