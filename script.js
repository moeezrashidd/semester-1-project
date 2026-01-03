
let products = [];


async function fetchProducts() {
  const response = await fetch("./productListForAICT.json");
  const data = await response.json();

  products = data;
  renderProducts();

}

function renderProducts() {
  const product_container = document.querySelector(".products-container-parent");
  product_container.innerHTML = "";
  products.forEach((item) => {
    product_container.innerHTML += `
      <div class="product-card" id="${item.id}" onclick="openProduct(${item.id})">
        <img src="${item.photo}" alt="pic of product">
        <div class="product-card-text">
          <span id="no-of-item">(${item.productNumber})</span>
          <span id="title">
            ${item.title.length > 45 ? item.title.slice(0, 45) + "..." : item.title}
          </span>
          <span id="price">PKR ${item.sellingCost} / <strike>PKR ${item.originalCost}</strike></span>
          <div class="shipingOpt">
            <span>FREE SHIPPING</span>
            <span>FREE GIFT</span>
          </div>
          <span id="inStock"><i class="fa-solid fa-check"></i> In Stock</span>
          <button class="add-cart-btn" onclick="event.stopPropagation(); addToCart(${item.id})">Add to Cart</button>
        </div>
      </div>
    `;
  });
}

fetchProducts();

const menuBtn = document.getElementById('menu-btn');
const mobileNav = document.getElementById('mobile-nav');

menuBtn.addEventListener('click', () => {
  mobileNav.classList.toggle('show');
});

function addToCart(id) {
  const currentUser = localStorage.getItem("currentUser");
  if (!currentUser) {
    alert("Please login to add items to cart");
    window.location.href = "./pages/signIn/signIn.html";
    return;
  }

  const product = products.find(p => p.id === id);
  if (!product) return;

  // Map to cart item format
  const cartItem = {
    id: String(product.id),
    title: product.title,
    price: product.sellingCost,
    originalPrice: product.originalCost,
    image: product.photo,
    quantity: 1
  };

  let cart = JSON.parse(localStorage.getItem('mh-cart')) || [];

  const existingItem = cart.find(item => item.id === cartItem.id);
  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    cart.push(cartItem);
  }

  localStorage.setItem('mh-cart', JSON.stringify(cart));
  alert('Item added to cart!');
  localStorage.setItem('mh-cart', JSON.stringify(cart));
  alert('Item added to cart!');
}

function openProduct(id) {
  localStorage.setItem('selectedProductId', id);
  window.location.href = './pages/product/product.html';
}
