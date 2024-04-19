// function updateTime() {
//     var currentTime = new Date();
//     var hours = currentTime.getHours();
//     var minutes = currentTime.getMinutes();
//     var seconds = currentTime.getSeconds();
//
//     // Добавляем нули к числам, если они состоят из одной цифры
//     minutes = (minutes < 10 ? "0" : "") + minutes;
//     seconds = (seconds < 10 ? "0" : "") + seconds;
//
//     // Форматируем время в строку и выводим на страницу
//     var timeString = hours + ":" + minutes + ":" + seconds;
//     document.getElementById("clock").innerText = timeString;
// }
//
// // Обновляем время каждую секунду
// setInterval(updateTime, 1000);
// // Обработчик изменения количества и выбора кофе
// document.getElementById("order-form").addEventListener("input", function () {
//     calculateTotal();
// });
//
// // Функция для подсчета итоговой стоимости заказа
// function calculateTotal() {
//     var coffeeSelect = document.getElementById("coffee");
//     var quantityInput = document.getElementById("quantity");
//     var totalSpan = document.getElementById("total");
//
//     var coffeePrice = parseInt(coffeeSelect.options[coffeeSelect.selectedIndex].dataset.price);
//     var quantity = parseInt(quantityInput.value);
//
//     var total = coffeePrice * quantity;
//     totalSpan.textContent = total; // Отображаем итоговую стоимость без дополнительного форматирования
// }
//
// // Обработчик отправки формы
// document.getElementById("order-form").addEventListener("submit", function (event) {
//     event.preventDefault(); // Предотвращаем стандартное поведение отправки формы
//
//     // Получаем значения из формы
//     var name = document.getElementById("name").value;
//     var email = document.getElementById("email").value;
//     var coffee = document.getElementById("coffee").value;
//     var quantity = document.getElementById("quantity").value;
//
//     // Создаем объект FormData для отправки данных на сервер
//     var formData = new FormData();
//     formData.append("name", name);
//     formData.append("email", email);
//     formData.append("coffee", coffee);
//     formData.append("quantity", quantity);
//
//     // Отправляем данные на сервер с помощью AJAX
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "обработчик_заказа.php", true); // Укажите путь к файлу обработчику заказа на сервере
//     xhr.onload = function () {
//         if (xhr.status === 200) {
//             // Здесь вы можете добавить логику для обработки ответа от сервера после успешной отправки заказа
//             alert("Ваш заказ успешно отправлен!");
//             // Очищаем форму после успешной отправки заказа
//             document.getElementById("order-form").reset();
//             document.getElementById("total").textContent = '0'; // Сбрасываем итоговую стоимость
//         } else {
//             // Здесь вы можете добавить логику для обработки ошибок отправки заказа
//             alert("Произошла ошибка при отправке заказа. Пожалуйста, попробуйте еще раз.");
//         }
//     };
//
//     xhr.send(formData);
//     // Добавляем алерт после успешной отправки заказа
//     alert("Ваш заказ успешно отправлен!");
// });
//
// // Симуляция изменения статуса заказа (можете изменить этот код на соответствующую логику вашего приложения)
// function updateOrderStatus() {
//     var statuses = ["Ожидается подтверждение", "В обработке", "На доставке", "Доставлен"];
//     var index = Math.floor(Math.random() * statuses.length);
//     var status = statuses[index];
//     document.getElementById("status").textContent = status;
// }
//
// // Обработчик нажатия на кнопку "Обновить статус"
// document.getElementById("update-status").addEventListener("click", function () {
//     updateOrderStatus();
// });
// document.getElementById("category").addEventListener("change", function () {
//     var category = this.value;
//     var dishes = document.querySelectorAll(".dish");
//
//     dishes.forEach(function (dish) {
//         var dishCategory = dish.getAttribute("data-category");
//
//         if (category === "all" || dishCategory === category) {
//             dish.style.display = "block";
//         } else {
//             dish.style.display = "none";
//         }
//     });
// });
// // Оценка
// document.querySelectorAll('.star').forEach(function (star) {
//     star.addEventListener('click', function () {
//         document.getElementById('rating-value').textContent = this.getAttribute('data-value');
//     });
// });
//
// // Отзыв
// document.getElementById('submit-review').addEventListener('click', function () {
//     var reviewText = document.getElementById('review-text').value;
//     // Отправить отзыв на сервер или выполнить другие действия
//     console.log('Отправлен отзыв:', reviewText);
//     alert('Ваш отзыв отправлен!');
// });