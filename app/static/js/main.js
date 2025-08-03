// Main JavaScript functionality

// Toast notifications
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `fixed top-4 right-4 z-50 p-4 rounded-md shadow-lg max-w-sm transition-all duration-300 transform translate-x-full ${
        type === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'
    }`;
    
    toast.innerHTML = `
        <div class="flex">
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'} mr-2 mt-0.5"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(toast);
    
    // Animate in
    setTimeout(() => {
        toast.classList.remove('translate-x-full');
    }, 100);
    
    // Auto hide after 5 seconds
    setTimeout(() => {
        toast.classList.add('translate-x-full');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 5000);
}

// Drag and drop functionality for list items
function initializeDragAndDrop() {
    const itemsList = document.getElementById('items-list');
    if (!itemsList) return;
    
    let draggedElement = null;
    
    itemsList.addEventListener('dragstart', function(e) {
        draggedElement = e.target.closest('.item-row');
        e.target.style.opacity = '0.5';
    });
    
    itemsList.addEventListener('dragend', function(e) {
        e.target.style.opacity = '';
        draggedElement = null;
    });
    
    itemsList.addEventListener('dragover', function(e) {
        e.preventDefault();
    });
    
    itemsList.addEventListener('drop', function(e) {
        e.preventDefault();
        const targetElement = e.target.closest('.item-row');
        
        if (targetElement && draggedElement && targetElement !== draggedElement) {
            const rect = targetElement.getBoundingClientRect();
            const midpoint = rect.top + rect.height / 2;
            
            if (e.clientY < midpoint) {
                itemsList.insertBefore(draggedElement, targetElement);
            } else {
                itemsList.insertBefore(draggedElement, targetElement.nextSibling);
            }
            
            // Update positions on server
            updateItemPositions();
        }
    });
    
    // Make items draggable
    document.querySelectorAll('.item-row').forEach(item => {
        item.draggable = true;
    });
}

// Update item positions after drag and drop
function updateItemPositions() {
    const items = document.querySelectorAll('.item-row');
    const positions = Array.from(items).map((item, index) => ({
        id: item.dataset.itemId,
        position: index
    }));
    
    const csrfToken = document.querySelector('meta[name=csrf-token]')?.getAttribute('content');
    fetch('/update_item_positions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ positions })
    })
    .catch(error => {
        console.error('Erro ao atualizar posições:', error);
    });
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + N for new list
    if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
        e.preventDefault();
        if (window.location.pathname === '/dashboard') {
            window.location.href = '/create_list';
        }
    }
    
    // Escape to close modals or go back
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        if (modals.length > 0) {
            modals.forEach(modal => modal.style.display = 'none');
        }
    }
});

// Auto-focus on first input field
document.addEventListener('DOMContentLoaded', function() {
    const firstInput = document.querySelector('input[type="text"], input[type="email"], textarea');
    if (firstInput) {
        firstInput.focus();
    }
    
    // Initialize drag and drop
    initializeDragAndDrop();
});

// Smooth checkbox animations
document.querySelectorAll('.item-checkbox').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const itemRow = this.closest('.item-row');
        itemRow.style.transition = 'all 0.3s ease';
        
        if (this.checked) {
            itemRow.style.opacity = '0.7';
        } else {
            itemRow.style.opacity = '1';
        }
    });
});

// Search functionality
function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        const items = document.querySelectorAll('.item-row');
        
        items.forEach(item => {
            const itemName = item.querySelector('.item-name').textContent.toLowerCase();
            const itemNotes = item.querySelector('.item-notes')?.textContent.toLowerCase() || '';
            
            if (itemName.includes(query) || itemNotes.includes(query)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
}

// Price calculator
function calculateTotal() {
    const items = document.querySelectorAll('.item-row');
    let total = 0;
    
    items.forEach(item => {
        const priceElement = item.querySelector('[data-price]');
        const quantityElement = item.querySelector('[data-quantity]');
        
        if (priceElement && quantityElement) {
            const price = parseFloat(priceElement.dataset.price) || 0;
            const quantity = parseFloat(quantityElement.dataset.quantity) || 1;
            total += price * quantity;
        }
    });
    
    const totalElement = document.getElementById('total-price');
    if (totalElement) {
        totalElement.textContent = `$${total.toFixed(2)}`;
    }
}

// Auto-save functionality
let autoSaveTimeout;
function autoSave() {
    clearTimeout(autoSaveTimeout);
    autoSaveTimeout = setTimeout(() => {
        // Implement auto-save logic here
        console.log('Auto-saving...');
    }, 2000);
}