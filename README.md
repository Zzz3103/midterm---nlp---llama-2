# LLAMA 2 - Nhóm 5
Nhóm chúng tôi đã triển khai một mô hình dựa trên LLaMA 2 với các thành phần chính sau:

Rotary Positional Embeddings (RoPE): Tính toán embedding theo góc quay bằng cách dùng số phức và phép biến đổi sin/cos.

RMS-Norm: Chuẩn hóa đầu vào bằng chuẩn trung bình bình phương để cải thiện ổn định huấn luyện.

LlamaLayer: Gồm normalization, attention, residual connection và mạng feedforward.

AdamW Optimizer: Áp dụng tối ưu hóa Adam kết hợp weight decay tách biệt rõ ràng.

Cơ chế Attention: Triển khai attention chuẩn với Q, K, V và normalization theo chiều key.

Hàm Generate: Sinh văn bản với temperature sampling và xử lý ngắt chuỗi động.

🔬 Các thiết lập và kết quả thử nghiệm:
Setting 1: Text continuation.

Setting 2: Zero-shot prompting với SST-5 và CFIMDB.

Setting 3: Fine-tuning phân loại tác vụ với SST-5 và CFIMDB.

Đã thử nghiệm với nhiều siêu tham số như dropout, n_layers, và n_kv_heads.
