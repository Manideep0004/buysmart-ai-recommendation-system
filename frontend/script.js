async function loadRec() {

    const res = await fetch(
        "http://127.0.0.1:8000/recommend/10"
    )

    const data = await res.json()

    const div = document.getElementById("products")

    div.innerHTML = ""

    data.forEach(p => {

        const card = document.createElement("div")

        card.className = "card"

        card.innerHTML = `
            <img src="${p.image[0]}" />
            <h3>${p.title}</h3>
        `

        div.appendChild(card)

    })

}