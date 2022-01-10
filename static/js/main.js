// var gallery = document.querySelector('.gallery');
// var getVal = function (elem, style) { return parseInt(window.getComputedStyle(elem).getPropertyValue(style)); };
// var getHeight = function (item) { return item.querySelector('.content').getBoundingClientRect().height; };
// var resizeAll = function () {
//     var altura = getVal(gallery, 'grid-auto-rows');
//     var gap = getVal(gallery, 'grid-row-gap');
//     gallery.querySelectorAll('.gallery-item').forEach(function (item) {
//         var el = item;
//         el.style.gridRowEnd = "span " + Math.ceil((getHeight(item) + gap) / (altura + gap));
//     });
// };
// // gallery.querySelectorAll('a').forEach(function (item) {
// //     item.classList.add('byebye');
// //     if (item.complete) {
// //         console.log(item.src);
// //     }
// //     else {
// //         item.addEventListener('load', function () {
// //             var altura = getVal(gallery, 'grid-auto-rows');
// //             var gap = getVal(gallery, 'grid-row-gap');
// //             var gitem = item.parentElement.parentElement;
// //             gitem.style.gridRowEnd = "span " + Math.ceil((getHeight(gitem) + gap) / (altura + gap));
// //             item.classList.remove('byebye');
// //         });
// //     }
// // });
// window.addEventListener('resize', resizeAll);
// gallery.querySelectorAll('.gallery-item').forEach(function (item) {
//     item.addEventListener('click', function () {        
//         item.classList.toggle('full');        
//     });
// });

// let thumbnails = document.getElementsByClassName('thumbnail')
// let activeImages = document.getElementsByClassName('active')
// for (var i=0; i < thumbnails.length; i++){
//     thumbnails[i].addEventListener('mouseover', function(){

//         if (activeImages.length > 0){
//             activeImages[0].classList.remove('active')
//         }

//         this.classList.add('active')
//         document.getElementById('featured').src = this.src
//     })
// }

// const buttonRight = document.getElementById('slideRight');
// const buttonLeft = document.getElementById('slideLeft');


// buttonRight.addEventListener('click', function(){
//     document.getElementById('slider').scrollLeft += 180;
// })



// buttonLeft.addEventListener('click', function(){
//     document.getElementById('slider').scrollLeft -= 180;
// })