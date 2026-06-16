// Theme and Animation Logic
const API_BASE = "http://localhost:8001";

let authToken = null;
let currentUserId = null;

document.addEventListener("DOMContentLoaded", () => {
    // Check for existing token
    authToken = localStorage.getItem("authToken");
    currentUserId = localStorage.getItem("userId");
    
    if (authToken) {
        updateAuthUI(true);
    } else {
        updateAuthUI(false);
    }

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

function updateAuthUI(isLoggedIn) {
    const authBtn = document.getElementById("authBtn");
    const recsBtn = document.getElementById("recsBtn");
    
    if (isLoggedIn) {
        authBtn.textContent = "Logout";
        authBtn.onclick = handleLogout;
        recsBtn.disabled = false;
        recsBtn.style.opacity = "1";
    } else {
        authBtn.textContent = "Login";
        authBtn.onclick = openAuthModal;
        recsBtn.disabled = true;
        recsBtn.style.opacity = "0.5";
    }
}

function openAuthModal() {
    document.getElementById("authModal").classList.remove("hidden");
}

function closeAuthModal() {
    document.getElementById("authModal").classList.add("hidden");
}

function switchTab(tab) {
    document.querySelectorAll(".auth-tab").forEach(t => t.classList.add("hidden"));
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    
    if (tab === "login") {
        document.getElementById("loginTab").classList.remove("hidden");
        document.querySelectorAll(".tab-btn")[0].classList.add("active");
    } else {
        document.getElementById("signupTab").classList.remove("hidden");
        document.querySelectorAll(".tab-btn")[1].classList.add("active");
    }
}

async function handleSignup() {
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;
    const errorEl = document.getElementById("signupError");
    errorEl.textContent = "";

    if (!email || !password) {
        errorEl.textContent = "Please fill in all fields";
        return;
    }

    try {
        const res = await fetch(`${API_BASE}/auth/signup`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (!res.ok) {
            const err = await res.json();
            errorEl.textContent = err.detail || "Signup failed";
            return;
        }

        const user = await res.json();
        currentUserId = user.id;
        localStorage.setItem("userId", user.id);
        
        // Auto-login after signup
        await handleLogin(email, password);
    } catch (err) {
        errorEl.textContent = "Signup error: " + err.message;
    }
}

async function handleLogin(email = null, password = null) {
    if (!email) email = document.getElementById("loginEmail").value;
    if (!password) password = document.getElementById("loginPassword").value;
    
    const errorEl = document.getElementById("loginError");
    errorEl.textContent = "";

    if (!email || !password) {
        errorEl.textContent = "Please fill in all fields";
        return;
    }

    try {
        const res = await fetch(`${API_BASE}/auth/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (!res.ok) {
            const err = await res.json();
            errorEl.textContent = err.detail || "Login failed";
            return;
        }

        const data = await res.json();
        authToken = data.access_token;
        localStorage.setItem("authToken", authToken);
        
        updateAuthUI(true);
        closeAuthModal();
        
        // Clear form
        document.getElementById("loginEmail").value = "";
        document.getElementById("loginPassword").value = "";
        document.getElementById("signupEmail").value = "";
        document.getElementById("signupPassword").value = "";
        
        // Load personalized recs
        loadPersonalizedRecs();
    } catch (err) {
        errorEl.textContent = "Login error: " + err.message;
    }
}

function handleLogout() {
    authToken = null;
    currentUserId = null;
    localStorage.removeItem("authToken");
    localStorage.removeItem("userId");
    updateAuthUI(false);
    closeAuthModal();
    loadRec();
}

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

async function loadPersonalizedRecs() {
    if (!authToken) {
        alert("Please login first");
        openAuthModal();
        return;
    }

    const div = document.getElementById("rec1");
    div.innerHTML = "<div class='loader-placeholder'></div>";
    
    try {
        const res = await fetch(`${API_BASE}/products/personalized`, {
            headers: { "Authorization": `Bearer ${authToken}` }
        });

        if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();
        render("rec1", data);
        
        // Scroll to personalized section
        document.getElementById('recommendedSection').scrollIntoView({ behavior: 'smooth' });
    } catch (err) {
        console.error("Failed to load personalized recs:", err);
        div.innerHTML = "<p class='error'>Failed to load personalized recommendations.</p>";
    }
}

function render(divId, data) {
    const div = document.getElementById(divId);
    div.innerHTML = "";

    if (!data || data.length === 0) {
        div.innerHTML = "<p class='error'>No products found.</p>";
        return;
    }

    data.forEach((p, i) => {
        const card = document.createElement("div");
        card.className = "card";
        // Staggered entry animation delay
        card.style.animationDelay = `${i * 0.05}s`;
        
        const imgSrc = p.image && p.image[0] ? p.image[0] : "https://via.placeholder.com/200?text=No+Image";
        
        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${imgSrc}" alt="${p.title}" loading="lazy" />
            </div>
            <div class="card-content">
                <h4 title="${p.title}">${p.title}</h4>
            </div>
        `;

        card.onclick = async () => {
            // Visual feedback on click
            card.style.transform = "scale(0.95)";
            setTimeout(() => card.style.transform = "", 100);

            // Track interaction
            if (authToken && currentUserId) {
                try {
                    await fetch(`${API_BASE}/products/interact/${p.product_id}`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": `Bearer ${authToken}`
                        },
                        body: JSON.stringify({ type: "view" })
                    });
                } catch (err) {
                    console.error("Interaction tracking failed:", err);
                }
            }

            // Load similar products
            if (authToken) {
                try {
                    const res = await fetch(`${API_BASE}/products/by-id/${p.product_id}`, {
                        headers: { "Authorization": `Bearer ${authToken}` }
                    });
                    const newData = await res.json();
                    render("rec4", newData);
                } catch (err) {
                    console.error("Failed to load similar products:", err);
                }
            } else {
                // Fallback without auth
                try {
                    const res = await fetch(`${API_BASE}/products/by-id/${p.product_id}`);
                    const newData = await res.json();
                    render("rec4", newData);
                } catch (err) {
                    console.error("Failed to load similar products:", err);
                }
            }
            
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