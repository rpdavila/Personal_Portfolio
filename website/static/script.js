//Project cards
let card_1 = document.getElementById('card-1')
let card_2 = document.getElementById('card-2')
let card_3 = document.getElementById('card-3')
let card_4 = document.getElementById('card-4')
let button_3 = document.getElementById('button3')

card_1.addEventListener('click', function() {
    window.location.href = "https://github.com/rpdavila/personal_portfolio";
} )

card_2.addEventListener('click', function() {
    window.location.href = "https://github.com/rpdavila/image-ai";
} )

card_3.addEventListener('click', function() {
    window.location.href = "https://github.com/zero-to-mastery/ascii-art";
} )

card_4.addEventListener('click', function() {
    window.location.href = "http://127.0.0.1:5000/twitter-api"
})

//twitter page buttons
// function makeVisible() {
//   let x = document.getElementById("graph-data");
//   if (x.style.display === "none") {
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
// }
//
// button_3.addEventListener('click', makeVisible )



