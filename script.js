const products = [
  {
    "productNumber": 201,
    "title": "Wireless Bluetooth Over-Ear Headphones with Noise Isolation and Mic",
    "sellingCost": 4500,
    "originalCost": 6000,
    "photo": "./assets/products/headphone.png"
  },
  {
    "productNumber": 202,
    "title": "Men’s Casual Slim-Fit Cotton Shirt for Daily and Office Wear",
    "sellingCost": 2200,
    "originalCost": 3000,
    "photo": "./assets/products/shirt.png"
  },
  {
    "productNumber": 203,
    "title": "Herbal Facial Cleanser with Neem and Aloe Vera for All Skin Types",
    "sellingCost": 850,
    "originalCost": 1200,
    "photo": "./assets/products/face wash.png"
  },
  {
    "productNumber": 204,
    "title": "43-Inch Smart LED Television with Full HD Display and Streaming Apps",
    "sellingCost": 65000,
    "originalCost": 72000,
    "photo": "./assets/products/led.png"
  },
  {
    "productNumber": 205,
    "title": "Women’s Premium Leather Handbag with Spacious Compartments",
    "sellingCost": 3800,
    "originalCost": 5000,
    "photo": "./assets/products/women purse.png"
  },
  {
    "productNumber": 206,
    "title": "Android Smartphone with 128GB Storage, Dual Camera, and Fast Charging",
    "sellingCost": 52000,
    "originalCost": 58000,
    "photo": "./assets/products/mobile.png"
  },
  {
    "productNumber": 207,
    "title": "Long-Lasting Men’s Perfume with Woody Fragrance (100ml Bottle)",
    "sellingCost": 3200,
    "originalCost": 4500,
    "photo": "./assets/products/perfume.png"
  },
  {
    "productNumber": 208,
    "title": "Lightweight Running Sports Shoes with Cushioned Sole for Comfort",
    "sellingCost": 5600,
    "originalCost": 7000,
    "photo": "./assets/products/sneaker.png"
  },
  {
    "productNumber": 209,
    "title": "Electric Kettle 1.7 Liter with Auto Shut-Off and Stainless Steel Body",
    "sellingCost": 2900,
    "originalCost": 3600,
    "photo": "./assets/products/kettle.png"
  },
  {
    "productNumber": 210,
    "title": "Matte Finish Lipstick Makeup Set with Multiple Shades for Daily Use",
    "sellingCost": 1800,
    "originalCost": 2500,
    "photo": "./assets/products/lipstick.png"
  }
]

let product_container = document.querySelector(".products-container-parent")

products.forEach((item)=>{
product_container.innerHTML += `
        <div class="product-card">
                <img src="${item.photo}" alt="pic of product">
                <div class="product-card-text">
                    <span id="no-of-item">(${item.productNumber})</span>
                    <span id="title">${item.title}</span>
                    <span id="price">PKR ${item.sellingCost} / <strike>PKR ${item.originalCost}</strike></span>
                    <div class="shipingOpt">
                        <span>FREE SHIPPING</span>
                        <span>FREE GIFT</span>
                    </div>
                    <span id="inStock"><i class="fa-solid fa-check"></i> In Stock</span>
                </div>
            </div>
`
})