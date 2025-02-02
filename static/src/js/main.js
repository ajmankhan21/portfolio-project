// Close alert messages
document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        $delete.addEventListener('click', () => {
            $delete.parentNode.remove();
        });
    });
});