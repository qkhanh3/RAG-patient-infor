Đây là hệ thống RAG (Retrieval-Augmented Generation) giúp tự động tạo thư giới thiệu y tế dựa trên ghi chú lâm sàng của bệnh nhân. Dự án chạy hoàn toàn cục bộ sử dụng LangChain, ChromaDB và Ollama.

Bước 1: Trích xuất dữ liệu
Đảm bảo bạn có file clinical_note.xlsx ở thư mục gốc. Chạy lệnh sau để tạo thư mục data và tách dữ liệu thành các file text:

Bash

mkdir data
python read_note.py
Bước 2: Xây dựng Vector Database
Đọc các file text, chia nhỏ (chunk) và lưu vào cơ sở dữ liệu Chroma:

Bash

python populate_database.py
(Mẹo: Thêm cờ --reset ở cuối lệnh trên nếu bạn muốn xóa data cũ và tạo lại từ đầu).

Bước 3: Chạy ứng dụng
Bạn có thể chọn 1 trong 3 cách sau để giao tiếp với hệ thống:

Cách 1: Giao diện Streamlit (Giao diện web đẹp, dễ dùng)

Bash

streamlit run app.py
Cách 2: Giao diện Gradio (Có thể chia sẻ link public)

Bash

python demo.py
Cách 3: Chạy trực tiếp trên Terminal (CLI)

Bash

python referral_bot.py "Nhập tình trạng của bệnh nhân vào đây..."
