function toggleItem(itemId) {
    const csrfToken = document.querySelector('meta[name=csrf-token]')?.getAttribute('content');
    fetch(`/toggle_item/${itemId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const itemRow = document.querySelector(`[data-item-id="${itemId}"]`);
            const itemName = itemRow.querySelector('.item-name');
            
            if (data.is_purchased) {
                itemName.classList.add('line-through', 'text-gray-600', 'dark:text-gray-400');
                itemName.classList.remove('text-gray-900', 'dark:text-white');
            } else {
                itemName.classList.remove('line-through', 'text-gray-600', 'dark:text-gray-400');
                itemName.classList.add('text-gray-900', 'dark:text-white');
            }
            
            // Update progress bar
            setTimeout(() => location.reload(), 500);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao atualizar item. Tente novamente.');
    });
}

function deleteItem(itemId) {
    if (confirm('Tem certeza que deseja excluir este item?')) {
        // Redireciona para a rota de delete usando um form temporário
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/delete_item/${itemId}`;
        
        // Adiciona o CSRF token
        const csrfToken = document.querySelector('meta[name=csrf-token]')?.getAttribute('content');
        if (csrfToken) {
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrf_token';
            csrfInput.value = csrfToken;
            form.appendChild(csrfInput);
        }
        
        document.body.appendChild(form);
        form.submit();
    }
}

function editItem(itemId, name, quantity, unit, price, notes, categoryId) {
    // Preenche o modal com os dados do item
    document.getElementById('edit-item-id').value = itemId;
    document.getElementById('edit-item-name').value = name;
    document.getElementById('edit-item-quantity').value = quantity;
    document.getElementById('edit-item-unit').value = unit;
    document.getElementById('edit-item-price').value = price;
    document.getElementById('edit-item-notes').value = notes;
    document.getElementById('edit-item-category').value = categoryId;
    
    // Mostra o modal
    document.getElementById('edit-modal').classList.remove('hidden');
}

// Event listeners para botões de editar e deletar
document.addEventListener('DOMContentLoaded', function() {
    // Update category colors on page load
    if (window.updateCategoryColors) {
        updateCategoryColors();
    }
    // Botões de editar
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            const name = this.getAttribute('data-item-name');
            const quantity = this.getAttribute('data-item-quantity');
            const unit = this.getAttribute('data-item-unit');
            const price = this.getAttribute('data-item-price');
            const notes = this.getAttribute('data-item-notes');
            const categoryId = this.getAttribute('data-item-category');
            
            editItem(itemId, name, quantity, unit, price, notes, categoryId);
        });
    });
    
    // Botões de deletar
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            deleteItem(itemId);
        });
    });
});

function closeEditModal() {
    document.getElementById('edit-modal').classList.add('hidden');
}