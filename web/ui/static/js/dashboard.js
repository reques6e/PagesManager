document.querySelector(".jsFilter").addEventListener("click", function () {
    document.querySelector(".filter-menu").classList.toggle("active");
});

// Меняет вреппер устройств
//document.querySelector(".grid").addEventListener("click", function () {
//     document.querySelector(".list").classList.remove("active");
//     document.querySelector(".grid").classList.add("active");
//     document.querySelector(".devices-area-wrapper").classList.add("gridView");
//     document.querySelector(".devices-area-wrapper").classList.remove("tableView");
// }); 

document.querySelector(".list").addEventListener("click", function () {
    document.querySelector(".list").classList.add("active");
    document.querySelector(".grid").classList.remove("active");
    document.querySelector(".devices-area-wrapper").classList.remove("gridView");
    document.querySelector(".devices-area-wrapper").classList.add("tableView");
});

var modeSwitch = document.querySelector('.mode-switch');
modeSwitch.addEventListener('click', function () {
    document.documentElement.classList.toggle('light');
    modeSwitch.classList.toggle('active');
});