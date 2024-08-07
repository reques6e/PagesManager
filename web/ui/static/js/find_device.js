document.getElementById('search-input').addEventListener('keypress', function(event) {
    // Проверяем, что нажата клавиша Enter (код клавиши 13)
    if (event.key === 'Enter') {
        event.preventDefault();  // Отменяем стандартное действие (например, отправку формы)
        const searchValue = document.getElementById('search-input').value;
        if (searchValue) {
            window.location.href = `/dashboard?find=${encodeURIComponent(searchValue)}`;
        }
    }
});