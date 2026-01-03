
const DUMMY_PRODUCTS = [
    {
        id: "p1",
        title: "Modern L-Shaped Sofa Bed with Storage - Premium Fabric Grey",
        price: 84990,
        originalPrice: 129999,
        image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400",
        quantity: 1
    },
    {
        id: "p2",
        title: "Luxury Round Marble Coffee Table - Black Metal Base",
        price: 32990,
        originalPrice: 45000,
        image: "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400",
        quantity: 1
    }
];

let cart = [];


document.addEventListener('DOMContentLoaded', () => {
    const currentUser = localStorage.getItem("currentUser");
    if (!currentUser) {
        alert("Please login to view your cart");
        window.location.href = "../signIn/signIn.html";
        return;
    }

    loadCart();
    renderCart();
});

function loadCart() {
    const savedCart = localStorage.getItem('mh-cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
    } else {

        cart = [...DUMMY_PRODUCTS];
        saveCart();
    }
}

function saveCart() {
    localStorage.setItem('mh-cart', JSON.stringify(cart));
    updateSummary();
}

function renderCart() {
    const container = document.getElementById('cart-items-container');
    const countElement = document.getElementById('cart-count');

    if (cart.length === 0) {
        container.innerHTML = `
            <div class="empty-cart">
                <i class="fa-solid fa-cart-shopping"></i>
                <p>Your cart is empty</p>
                <a href="../../index.html" class="btn-shop">Start Shopping</a>
            </div>
        `;
        countElement.innerText = "(0 Items)";
        updateSummary();
        return;
    }

    countElement.innerText = `(${cart.reduce((acc, item) => acc + item.quantity, 0)} Items)`;

    container.innerHTML = cart.map(item => `
        <div class="cart-item" data-id="${item.id}">
            <div class="cart-item-inner">
                <img src="${item.image.startsWith('./') ? item.image.replace('./', '../../') : item.image}" alt="${item.title}" class="item-image">
                <div class="item-details">
                    <div class="item-title">${item.title}</div>
                    
                    <div class="price-row">
                        <span class="item-price">Rs. ${item.price.toLocaleString()}</span>
                        ${item.originalPrice ? `<span class="item-old-price">Rs. ${item.originalPrice.toLocaleString()}</span>` : ''}
                    </div>

                    <div class="quantity-control">
                        <button class="qty-btn" onclick="updateQuantity('${item.id}', -1)">-</button>
                        <span class="qty-val">${item.quantity}</span>
                        <button class="qty-btn" onclick="updateQuantity('${item.id}', 1)">+</button>
                    </div>
                </div>
            </div>
            <button class="delete-btn" onclick="removeItem('${item.id}')" title="Remove item">
                <i class="fas fa-trash-alt"></i>
            </button>
        </div>
    `).join('');

    updateSummary();
}

function updateQuantity(id, change) {
    const itemIndex = cart.findIndex(item => item.id === id);
    if (itemIndex === -1) return;

    const item = cart[itemIndex];
    const newQuantity = item.quantity + change;

    if (newQuantity <= 0) {
        removeItem(id);
    } else {
        item.quantity = newQuantity;
        saveCart();
        renderCart();
    }
}

function removeItem(id) {
    if (!confirm("Are you sure you want to remove this item?")) return;

    cart = cart.filter(item => item.id !== id);
    saveCart();
    renderCart();
}

function updateSummary() {
    const subtotal = cart.reduce((acc, item) => acc + (item.price * item.quantity), 0);
    const totalElement = document.getElementById('cart-total');
    const subtotalElement = document.getElementById('cart-subtotal');

    if (subtotalElement) subtotalElement.innerText = `Rs. ${subtotal.toLocaleString()}`;
    if (totalElement) totalElement.innerText = `Rs. ${subtotal.toLocaleString()}`;
}


window.updateQuantity = updateQuantity;
window.removeItem = removeItem;
