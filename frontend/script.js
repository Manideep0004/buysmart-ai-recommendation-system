// Theme and Animation Logic
const API_BASE = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", () => {
    // Initial Load
    loadRec();

    // Scroll Animations using Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.rec-section').forEach(section => {
        observer.observe(section);
    });
});

async function loadRec() {
    loadRow("rec1", 10);
    loadRow("rec2", 20);
    loadRow("rec3", 30);
    loadUser();
}

async function loadRow(divId, index) {
    const div = document.getElementById(divId);
    div.innerHTML = "<div class='loader-placeholder'></div>";
    
    try {
        const res = await fetch(`${API_BASE}/products/${index}`);
        const data = await res.json();
        render(divId, data);
    } catch (err) {
        console.error("Failed to load row:", err);
        div.innerHTML = "<p class='error'>Failed to load recommendations.</p>";
    }
}

function render(divId, data) {
    const div = document.getElementById(divId);
    div.innerHTML = "";

    data.forEach((p, i) => {
        const card = document.createElement("div");
        card.className = "card";
        // Staggered entry animation delay
        card.style.animationDelay = `${i * 0.05}s`;
        
        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${p.image[0]}" alt="${p.title}" loading="lazy" />
            </div>
            <div class="card-content">
                <h4 title="${p.title}">${p.title}</h4>
            </div>
        `;

        card.onclick = async () => {
            // Visual feedback on click
            card.style.transform = "scale(0.95)";
            setTimeout(() => card.style.transform = "", 100);

            const res = await fetch(`${API_BASE}/products/by-id/${p.product_id}`);
            const newData = await res.json();
            render("rec4", newData);
            
            // Scroll to similar products section
            document.getElementById('similarProductsSection').scrollIntoView({ behavior: 'smooth' });
        };

        div.appendChild(card);
    });
}

async function loadUser() {
    try {
        const res = await fetch(`${API_BASE}/products/search/popular`);
        const data = await res.json();
        render("rec6", data);
    } catch (err) {
        console.error("Failed to load user recs:", err);
    }
}

async function loadUserRec() {
    const uid = document.getElementById("userInput").value;
    if (!uid) return;

    const btn = document.querySelector(".btn-secondary");
    btn.innerHTML = "<i class='fa-solid fa-circle-notch fa-spin'></i>";
    
    try {
        const res = await fetch(`${API_BASE}/products/search/${uid}`);
        const data = await res.json();
        render("rec6", data);
    } catch (err) {
        console.error("User rec failed:", err);
    } finally {
        btn.innerHTML = "Get Recs";
    }
}

async function searchProduct() {
    const q = document.getElementById("searchInput").value;
    if (!q) return;

    const btn = document.querySelector(".btn-primary");
    btn.innerHTML = "<i class='fa-solid fa-circle-notch fa-spin'></i>";

    try {
        const res = await fetch(`${API_BASE}/products/search/${q}`);
        const data = await res.json();
        render("rec1", data);
        
        // Scroll to results
        document.getElementById('recommendedSection').scrollIntoView({ behavior: 'smooth' });
    } catch (err) {
        console.error("Search failed:", err);
    } finally {
        btn.innerHTML = "Search";
    }
}