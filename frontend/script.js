async function loadRec() {

    loadRow("rec1", 10)
    loadRow("rec2", 20)
    loadRow("rec3", 30)

    loadPopular()
    loadUser()

}

async function loadRow(divId, index) {

    const res = await fetch(
        `https://buysmart-api-kqj5.onrender.com/recommend/${index}`
    )

    const data = await res.json()

    render(divId, data)

}

function render(divId, data) {

    const div =
        document.getElementById(divId)

    div.innerHTML = ""

    data.forEach(p => {

        const card =
            document.createElement("div")

        card.className = "card"

        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${p.image[0]}" alt="${p.title}" loading="lazy" />
            </div>
            <div class="card-content">
                <h4 title="${p.title}">${p.title}</h4>
            </div>
        `

        card.onclick = async () => {

            const res = await fetch(
                `https://buysmart-api-kqj5.onrender.com/recommend_by_id/${p.product_id}`
            )

            const newData = await res.json()

            render("rec4", newData)

        }

        div.appendChild(card)

    })

}

async function loadUser() {

    const res = await fetch(
        "https://buysmart-api-kqj5.onrender.com/recommend_user/A4V3MZPLN3XUU"
    )

    const data = await res.json()

    render("rec6", data)

}

async function loadUserRec() {

    const uid =
        document.getElementById("userInput").value

    if (!uid) return

    const res = await fetch(
        `https://buysmart-api-kqj5.onrender.com/recommend_user/${uid}`
    )

    const data = await res.json()

    render("rec6", data)

}

async function searchProduct() {

    const q =
        document.getElementById(
            "searchInput"
        ).value

    const res = await fetch(
        `https://buysmart-api-kqj5.onrender.com/search/${q}`
    )

    const data = await res.json()

    render("rec1", data)

}