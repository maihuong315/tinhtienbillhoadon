<!-- ==============================
     TÍNH TIỀN HÓA ĐƠN
================================ -->

<div class="invoice-box">

    <h2>🧾 Hóa đơn thanh toán</h2>

    <label>Giá phòng / đêm</label>
    <input type="number" id="roomPrice" value="1850000">

    <label>Số đêm</label>
    <input type="number" id="nights" value="2" min="1">

    <label>Phụ thu</label>
    <input type="number" id="surcharge" value="0">

    <label>Ăn sáng</label>
    <input type="number" id="breakfast" value="0">

    <label>Dịch vụ khác</label>
    <input type="number" id="services" value="0">

    <label>Giảm giá (%)</label>
    <input type="number" id="discount" value="0" min="0" max="100">

    <label>VAT (%)</label>
    <input type="number" id="vat" value="8" min="0">

    <label>Khách đã thanh toán</label>
    <input type="number" id="paid" value="0">

    <button onclick="calculateInvoice()">
        Tính hóa đơn
    </button>

    <div id="invoiceResult"></div>

</div>


<style>

.invoice-box {
    max-width: 500px;
    margin: 30px auto;
    padding: 25px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.1);
}

.invoice-box h2 {
    margin-bottom: 20px;
}

.invoice-box label {
    display: block;
    margin-top: 12px;
    font-weight: 600;
}

.invoice-box input {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-sizing: border-box;
}

.invoice-box button {
    width: 100%;
    margin-top: 20px;
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: #176b87;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

.invoice-result {
    margin-top: 25px;
}

.invoice-line {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

.invoice-total {
    font-size: 20px;
    font-weight: bold;
    margin-top: 15px;
}

.remaining {
    color: #d35400;
    font-weight: bold;
}

</style>


<script>

function formatMoney(amount) {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(amount);
}


function calculateInvoice() {

    // Lấy dữ liệu
    const roomPrice =
        Number(document.getElementById("roomPrice").value) || 0;

    const nights =
        Number(document.getElementById("nights").value) || 0;

    const surcharge =
        Number(document.getElementById("surcharge").value) || 0;

    const breakfast =
        Number(document.getElementById("breakfast").value) || 0;

    const services =
        Number(document.getElementById("services").value) || 0;

    const discountPercent =
        Number(document.getElementById("discount").value) || 0;

    const vatPercent =
        Number(document.getElementById("vat").value) || 0;

    const paid =
        Number(document.getElementById("paid").value) || 0;


    // 1. Tiền phòng
    const roomTotal = roomPrice * nights;


    // 2. Tổng trước giảm giá
    const subtotal =
        roomTotal +
        surcharge +
        breakfast +
        services;


    // 3. Tiền giảm giá
    const discountAmount =
        subtotal * discountPercent / 100;


    // 4. Sau giảm giá
    const afterDiscount =
        subtotal - discountAmount;


    // 5. VAT
    const vatAmount =
        afterDiscount * vatPercent / 100;


    // 6. Tổng hóa đơn
    const grandTotal =
        afterDiscount + vatAmount;


    // 7. Còn phải thu
    const remaining =
        grandTotal - paid;


    // Hiển thị hóa đơn
    document.getElementById("invoiceResult").innerHTML = `

        <div class="invoice-result">

            <div class="invoice-line">
                <span>Tiền phòng</span>
                <strong>${formatMoney(roomTotal)}</strong>
            </div>

            <div class="invoice-line">
                <span>Phụ thu</span>
                <strong>${formatMoney(surcharge)}</strong>
            </div>

            <div class="invoice-line">
                <span>Ăn sáng</span>
                <strong>${formatMoney(breakfast)}</strong>
            </div>

            <div class="invoice-line">
                <span>Dịch vụ khác</span>
                <strong>${formatMoney(services)}</strong>
            </div>

            <div class="invoice-line">
                <span>Tạm tính</span>
                <strong>${formatMoney(subtotal)}</strong>
            </div>

            <div class="invoice-line">
                <span>Giảm giá</span>
                <strong>
                    - ${formatMoney(discountAmount)}
                </strong>
            </div>

            <div class="invoice-line">
                <span>VAT ${vatPercent}%</span>
                <strong>${formatMoney(vatAmount)}</strong>
            </div>

            <div class="invoice-line invoice-total">
                <span>TỔNG CỘNG</span>
                <strong>${formatMoney(grandTotal)}</strong>
            </div>

            <div class="invoice-line">
                <span>Đã thanh toán</span>
                <strong>${formatMoney(paid)}</strong>
            </div>

            <div class="invoice-line remaining">
                <span>CÒN PHẢI THU</span>
                <strong>${formatMoney(Math.max(remaining, 0))}</strong>
            </div>

        </div>

    `;
}

</script>
