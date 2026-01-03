
document.addEventListener('DOMContentLoaded', () => {
    const selectedProductId = localStorage.getItem('selectedProductId');

    if (!selectedProductId) {
        window.location.href = '../../index.html';
        return;
    }

    fetch('../../productListForAICT.json')
        .then(response => response.json())
        .then(products => {
            const product = products.find(p => p.id == selectedProductId);

            if (product) {
                renderProductDetails(product);
                // Hide loader and show content
                document.getElementById('pageLoader').style.display = 'none';
                const content = document.getElementById('productContent');
                content.classList.remove('hidden-content');
                content.classList.add('fade-in');
            } else {
                document.getElementById('pageLoader').style.display = 'none';
                document.querySelector('.product-container').innerHTML = '<h2>Product not found</h2>';
            }
        })
        .catch(error => console.error('Error loading product:', error));
});

function renderProductDetails(product) {
    document.getElementById('mainProductImage').src = product.photo.replace('./', '../../'); // Adjust visual path if needed, or keep as is if absolute
    document.getElementById('mainProductImage').alt = product.title;

    document.getElementById('productTitle').innerText = product.title;
    document.getElementById('productDescription').innerText = product.description;

    document.getElementById('sellingPrice').innerText = `Rs. ${product.sellingCost.toLocaleString()}`;
    document.getElementById('originalPrice').innerText = `Rs. ${product.originalCost.toLocaleString()}`;

    // Calculate Discount
    const discount = Math.round(((product.originalCost - product.sellingCost) / product.originalCost) * 100);
    document.querySelector('.discount').innerText = `${discount}% OFF`;

    // Add to Cart Logic
    const addToCartBtn = document.getElementById('addToCartBtn');
    addToCartBtn.onclick = () => {
        addToCart(product);
    };
}

function addToCart(product) {
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
}
