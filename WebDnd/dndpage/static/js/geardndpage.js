function removeItem(button) {
    // Находим родительский элемент (div с классом item)
    const item = button.parentElement;
    // Удаляем элемент из DOM
    item.remove();
}

function increaseQuantity(button) {
    // Находим элемент с количеством
    const quantityElement = button.previousElementSibling;
    let quantity = parseInt(quantityElement.textContent); // Получаем текущее значение
    quantityElement.textContent = quantity + 1; // Увеличиваем на 1
}

function decreaseQuantity(button) {
    // Находим элемент с количеством
    const quantityElement = button.nextElementSibling;
    let quantity = parseInt(quantityElement.textContent); // Получаем текущее значение
    if (quantity > 0) {
        quantityElement.textContent = quantity - 1; // Уменьшаем на 1, если больше 0
    }
    if (quantity === 0) {
        const item = button.parentElement.parentElement;
        item.remove();
    } 
}