
async function loadRec() {

    loadRow("rec1", 10)
    loadRow("rec2", 20)
    loadRow("rec3", 30)

}

async function loadRow(divId, index) {

    const res = await fetch(
        `http://127.0.0.1:8000/recommend/${index}`
    )

    const data = await res.json()

    const div =
        document.getElementById(divId)

    div.innerHTML = ""

    data.forEach(p => {

        const card =
            document.createElement("div")

        card.className = "card"

        card.innerHTML = `
            <img src="${p.image[0]}" />
            <h4>${p.title}</h4>
        `

        card.onclick = () => {
            loadRow("rec4", index)
        }

        div.appendChild(card)

    })

}