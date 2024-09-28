import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title('Biểu đồ hàm số y = tan(x)')

# Tạo dãy giá trị x từ -2π đến 2π (với khoảng cách nhỏ để biểu diễn liên tục)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Tính giá trị y = tan(x)
y = np.tan(x)

# Tạo biểu đồ
fig, ax = plt.subplots()

# Vẽ hàm tan(x)
ax.plot(x, y, label='y = tan(x)')

# Giới hạn giá trị y để tránh các điểm giá trị rất lớn gần các đường tiệm cận
ax.set_ylim([-10, 10])

# Thêm đường lưới
ax.grid(True)

# Thêm tiêu đề và nhãn trục
ax.set_title('Biểu đồ hàm số y = tan(x)')
ax.set_xlabel('x (radian)')
ax.set_ylabel('y')

# Hiển thị biểu đồ trên Streamlit
st.pyplot(fig)
